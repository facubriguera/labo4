from fastapi import APIRouter
from typing import List
from schemas.inscripciones import InscripcionSchema
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from config.database import Session
from models.inscriptions import InscripcionModel
from services.inscriptionServices import InscripcionService
from utils.validators import validar_cupos_disponibles

inscription_router = APIRouter()

@inscription_router.get('/inscripciones', tags=['Inscriptions'], response_model=List[InscripcionSchema], status_code=200)
def get_inscripciones():
    db = Session()
    result = InscripcionService(db).get_inscripciones()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@inscription_router.get('/inscripciones/{id}', tags=['Inscriptions'], response_model=dict)
def get_inscripcion(inscrip_id: int):
    db = Session()
    result = InscripcionService(db).get_inscripcion(inscrip_id)
    if not result:
        return JSONResponse(status_code=404, content={'message': "No se ha encontrado"})
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@inscription_router.post('/inscripciones', tags=['Inscriptions'], response_model=dict, status_code=201)
def create_inscripcion(inscripcion: InscripcionSchema):
    db = Session()
    validar_cupos_disponibles(db, inscripcion.event_id)
    InscripcionService(db).create_inscripcion(inscripcion)
    return JSONResponse(status_code=201, content={"message": "La inscripcion ha sido registrada"})

@inscription_router.put('/inscripciones/{id}', tags=['Inscriptions'], response_model=dict, status_code=200)
def update_inscripcion(inscrip_id: int, inscripcion: InscripcionSchema):
    db = Session()
    result = InscripcionService(db).get_inscripcion(inscrip_id)
    if not result:
        return JSONResponse(status_code=404, content={'message': "No encontrado"})
    
    InscripcionService(db).update_inscripcion(inscrip_id, inscripcion)
    return JSONResponse(status_code=200, content={"message": "La inscripcion se ha modificado"})

@inscription_router.delete('/inscripciones/{id}', tags=['Inscriptions'], response_model=dict, status_code=200)
def delete_inscripcion(id: int):
    db = Session()
    result: InscripcionModel = db.query(InscripcionModel).filter(InscripcionModel.id == id).first()
    if not result:
        return JSONResponse(status_code=404, content={'message': "No encontrado"})
    InscripcionService(db).delete_inscripcion(id)
    return JSONResponse(status_code=200, content={"message": "Se ha eliminado la inscripcion"})

@inscription_router.get('/inscripciones/usuario/{user_id}', tags=['Inscriptions'], response_model=dict)
def get_inscripcion_usuario(user_id: int):
    db = Session()
    result = InscripcionService(db).get_inscripcion_usuario(user_id)
    if not result:
        return JSONResponse(status_code=404, content={'message': "No se han encontrado inscripciones de este usuario"})
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@inscription_router.get('/inscripciones/usuario/{user_id}', tags=['Inscriptions'], response_model=dict)
def get_inscripcion_usuario_activa(user_id: int):
    db = Session()
    result = InscripcionService(db).get_inscripcion_usuario_activa(user_id)
    if not result:
        return JSONResponse(status_code=404, content={'message': "El usuario no tiene inscripciones activas"})
    return JSONResponse(status_code=200, content=jsonable_encoder(result))