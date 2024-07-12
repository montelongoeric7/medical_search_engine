from fastapi import APIRouter, HTTPException, Depends, status, File, UploadFile
from sqlalchemy.orm import Session
import app.modelos.models as models
import app.schemasstuff.schemas as schemas
from app.dbs.database import get_db
import app.oauth.oauth2 as oauth2
from typing import List
import fitz
import os
from app.configurations.config import settings
import openai
import shutil
from openai import OpenAI
router = APIRouter(
    prefix="/information",
    tags=["Information"],
)


UPLOAD_DIRECTORY = "./uploaded_pdfs"

if not os.path.exists(UPLOAD_DIRECTORY):
    os.makedirs(UPLOAD_DIRECTORY)



def extract_text_from_pdf(file_path:str):
    text=""
    document =fitz.open(file_path)
    for page_num in range(len(document)):
        page= document.load_page(page_num)
        text+=page.get_text()
    return text


def summarize_text(text: str):
    client = OpenAI(api_key=settings.openai_api_key)
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that summarizes text."},
            {"role": "user", "content": f"Summarize the following text:\n\n{text}"}
        ],
        max_tokens=100
    )
    summary = response.choices[0].message.content.strip()
    return summary

@router.post("/upload-pdf", status_code=status.HTTP_201_CREATED)
async def upload_and_summarize_pdf(file: UploadFile = File(...), current_user: models.User = Depends(oauth2.get_current_user), db: Session = Depends(get_db)):
    if not file.filename.endswith(".pdf"):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Only PDF files are allowed.")
    
    file_path = os.path.join(UPLOAD_DIRECTORY, file.filename)
    
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    extracted_text = extract_text_from_pdf(file_path)
    summarized_text = summarize_text(extracted_text)
    
    new_information = models.Information(title=file.filename, content=summarized_text, user_id=current_user.id)
    db.add(new_information)
    db.commit()
    db.refresh(new_information)
    
    return {"filename": file.filename, "summary": summarized_text}


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.InformationOut)
def create_information(information: schemas.InformationCreate, db: Session = Depends(get_db), current_user: models.User = Depends(oauth2.get_current_user)):
    new_information = models.Information(**information.dict(), user_id=current_user.id)
    db.add(new_information)
    db.commit()
    db.refresh(new_information)
    return new_information

@router.get("/{id}", response_model=schemas.InformationOut)
def get_information(id: int, db: Session = Depends(get_db), current_user: models.User = Depends(oauth2.get_current_user)):
    information = db.query(models.Information).filter(models.Information.id == id).first()
    if not information:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Information not found")
    if information.user_id != current_user.id and not current_user.is_admin:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized to access this information")
    return information

@router.get("/", response_model=List[schemas.InformationOut])
def get_informations(db: Session = Depends(get_db), current_user: models.User = Depends(oauth2.get_current_user)):
    if current_user.is_admin:
        informations = db.query(models.Information).all()
    else:
        informations = db.query(models.Information).filter(models.Information.user_id == current_user.id).all()
    return informations


@router.put("/{id}", response_model=schemas.InformationOut)
def update_information(id: int, updated_info: schemas.InformationCreate, db: Session = Depends(get_db), current_user: models.User = Depends(oauth2.get_current_user)):
    information_query = db.query(models.Information).filter(models.Information.id == id)
    information = information_query.first()
    if not information:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Information not found")
    if information.user_id != current_user.id and not current_user.is_admin:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized to update this information")
    information_query.update(updated_info.dict(),synchronize_session=False)
    db.commit()
    db.refresh(information)
    return information



