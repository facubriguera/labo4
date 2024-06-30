from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from datetime import date
from config.database import Session
from services.inscriptionServices import InscriptionService
from schemas.inscripciones import InscriptionCreate, InscriptionHistory

inscription_router = APIRouter()

def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()

@inscription_router.get('/inscriptions/{user_id}/active', response_model=list, tags=['Inscriptions'])
def get_active_inscriptions(user_id: int, db: Session = Depends(get_db)):
    inscriptions = InscriptionService(db).get_active_inscriptions(user_id)
    return inscriptions

@inscription_router.get('/inscriptions/{user_id}/history', response_model=list, tags=['Inscriptions'])
def get_inscription_history(user_id: int, db: Session = Depends(get_db)):
    history = InscriptionService(db).get_inscription_history(user_id)
    return history

@inscription_router.post('/inscriptions', response_model=int, status_code=201, tags=['Inscriptions'])
def create_inscription(inscription: InscriptionCreate, db: Session = Depends(get_db)):
    return InscriptionService(db).create_inscription(inscription)

@inscription_router.delete('/inscriptions/{inscrip_id}', response_model=dict, tags=['Inscriptions'])
def delete_inscription(inscrip_id: int, db: Session = Depends(get_db)):
    return InscriptionService(db).delete_inscription(inscrip_id)
