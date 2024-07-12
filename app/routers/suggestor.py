from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
import app.modelos.models as models
import app.schemasstuff.schemas as schemas
from app.dbs.database import get_db
import app.oauth.oauth2 as oauth2
from typing import List

router = APIRouter(
    prefix="/suggestor",
    tags=["Suggestor"],
)

@router.post("/suggest", response_model=List[schemas.ClinicOut])
def suggest_clinics(potential_causes: schemas.ChatbotResponse, db: Session = Depends(get_db), current_user: models.User = Depends(oauth2.get_current_user)):
    causes_list = potential_causes.potential_causes.split('\n0')
    clinics = db.query(models.Clinic).all()
    suggested_clinics = []

    for clinic in clinics:
        clinic_services = clinic.services.split('\n')
        for cause in causes_list:
            if cause in clinic_services:
                suggested_clinics.append(clinic)
                break
    if not suggest_clinics:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No clinics found for the potential causes")
    return suggested_clinics

