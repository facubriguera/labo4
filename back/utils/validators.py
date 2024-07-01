from fastapi.exceptions import HTTPException
from typing import List
from sqlalchemy.orm import Session
from fastapi import HTTPException
from models.events import Events
from models.inscriptions import InscripcionModel

def idDuplicados(obj, lista:List):
        for item in lista:
            if item.id == obj.id :
                raise HTTPException(status_code=409,
                            detail=f"El id ya se encuentra registrado" )
            
def emailDuplicado(obj, lista:List):
        for item in lista:
            if item.email == obj.email:
                raise HTTPException(status_code=409,
                            detail=f"El email ya se encuentra registrado" )
            
def validar_cupos_disponibles(db: Session, event_id: int):
    evento = db.query(Events).filter(Events.id == event_id).first()
    
    inscripciones_actuales = db.query(InscripcionModel).filter(InscripcionModel.event_id == event_id).count()
    
    if inscripciones_actuales >= evento.cupos:
        raise HTTPException(status_code=400, detail="No hay cupos disponibles para este evento")