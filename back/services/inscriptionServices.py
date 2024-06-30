from typing import List
from datetime import date
from sqlalchemy.orm import Session
from models.inscriptions import Inscriptions as InscriptionModel
from schemas.inscripciones import InscriptionCreate, InscriptionHistory

class InscriptionService:
    def __init__(self, db: Session) -> None:
        self.db = db

    def get_active_inscriptions(self, user_id: int) -> List[InscriptionModel]:
        today = date.today()
        active_inscriptions = self.db.query(InscriptionModel).filter(
            InscriptionModel.user_id == user_id,
            InscriptionModel.fecha_inscripcion <= today,
            InscriptionModel.event_id.in_(
                self.db.query(InscriptionModel.event_id).distinct()
            )
        ).all()
        return active_inscriptions

    def get_inscription_history(self, user_id: int) -> List[InscriptionHistory]:
        today = date.today()
        history = self.db.query(InscriptionModel).filter(
            InscriptionModel.user_id == user_id,
            InscriptionModel.fecha_inscripcion > today
        ).all()
        return history

    def create_inscription(self, inscription: InscriptionCreate) -> int:
        new_inscription = InscriptionModel(**inscription.dict())
        self.db.add(new_inscription)
        self.db.commit()
        return new_inscription.inscrip_id

    def delete_inscription(self, inscrip_id: int) -> dict:
        inscription = self.db.query(InscriptionModel).filter(InscriptionModel.inscrip_id == inscrip_id).first()
        if inscription:
            self.db.delete(inscription)
            self.db.commit()
            return {"message": "Inscripción eliminada correctamente"}
        else:
            return {"message": "Inscripción no encontrada"}

