from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
import app.modelos.models as models
import app.schemasstuff.schemas as schemas
from app.dbs.database import get_db
import app.oauth.oauth2 as oauth2
from app.configurations.config import settings
import openai
from langchain_community.llms import OpenAI
# from app.routers.medical import query_medical2

router = APIRouter(
    prefix="/chatbot",
    tags=["Chatbot"],
)

openai.api_key = settings.openai_api_key

def get_potential_causes(user_info: str) -> str:
    llm = OpenAI(api_key=openai.api_key)
    prompt = f"You are a medical chatbot expert. Given the following symptoms, provide a list of five potential causes in a numbered list format:\n\n{user_info}"
    response = llm(prompt)
    causes = response.split('\n')
    formatted_causes = []
    for index, cause in enumerate(causes, 1):
        formatted_causes.append(f"{index}.) {cause.strip()}")

    return "\n".join(formatted_causes)


def get_potential_causes2(user_info: str) -> str:
    llm = OpenAI(api_key=openai.api_key)
    prompt = f"You are a medical chatbot expert robot. Given the following symptoms, provide a potential medical cause diagnosis that generally covers what might be happenind for {user_info}"
    response = llm(prompt)
    response2="".join(response.split("\n")[1:])
    return response2



@router.post("/diagnose", response_model=schemas.ChatbotResponse)
def diagnose(current_user: models.User = Depends(oauth2.get_current_user), db: Session = Depends(get_db)):
    user_info = db.query(models.Information).filter(models.Information.user_id == current_user.id).all()

    if not user_info:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No information found for the current user")

    user_info_str = "\n".join([f"Title: {info.title}, Content: {info.content}" for info in user_info])
    potential_causes = get_potential_causes(user_info_str)

    return {"potential_causes": potential_causes}

# @router.post("/suggestor2", response_model=schemas.ChatbotResponse)
# def suggestor(current_user: models.User = Depends(oauth2.get_current_user), db: Session = Depends(get_db)):
#     user_info = db.query(models.Information).filter(models.Information.user_id == current_user.id).all()

#     if not user_info:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No information found for the current user")

#     user_info_str = "\n".join([f"Title: {info.title}, Content: {info.content}" for info in user_info])
#     potential_cause = get_potential_causes2(user_info_str)
#     clinic = query_medical2(potential_cause)
#     return {"potential_cause": potential_cause, "clinic": clinic}
    