from fastapi import APIRouter
from fastapi import Depends, Path, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import Optional, List
from config.database import Session
from models.events import Events as EventModel
from fastapi.encoders import jsonable_encoder
from middlewares.jwt_bearer import JWTBearer
from services.eventsServices import EventService
from schemas.eventos import Events

event_router = APIRouter()


@event_router.get('/events', tags=['eventos'], response_model=List[Events], status_code=200, dependencies=[Depends(JWTBearer())])
def get_events() -> List[Events]:
    db = Session()
    result = EventService(db).get_event()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


@event_router.get('/events/{id}', tags=['eventos'], response_model=Events)
def get_event(id: int = Path(ge=1, le=2000)) -> Events:
    db = Session()
    result = EventService(db).get_event(id)
    if not result:
        return JSONResponse(status_code=404, content={'message': "No encontrado"})
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


@event_router.get('/events/', tags=['eventos'], response_model=List[Events])
def get_events_by_category(category: str = Query(min_length=1, max_length=15)) -> List[Events]:
    db = Session()
    result = EventService(db).get_events_by_category(category)
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


@event_router.post('/events', tags=['eventos'], response_model=dict, status_code=201)
def create_event(event: Events) -> dict:
    db = Session()
    EventService(db).create_event(event)
    return JSONResponse(status_code=201, content={"message": "Se ha registrado el evento."})


@event_router.put('/events/{id}', tags=['eventos'], response_model=dict, status_code=200)
def update_event(id: int, event: Events)-> dict:
    db = Session()
    result = EventService(db).get_event(id)
    if not result:
        return JSONResponse(status_code=404, content={'message': "No encontrado"})
    
    EventService(db).update_event(id, event)
    return JSONResponse(status_code=200, content={"message": "Se ha modificado el evento."})


@event_router.delete('/events/{id}', tags=['eventos'], response_model=dict, status_code=200)
def delete_event(id: int)-> dict:
    db = Session()
    result: EventModel = db.query(EventModel).filter(EventModel.id == id).first()
    if not result:
        return JSONResponse(status_code=404, content={"message": "No se encontró"})
    EventService(db).delete_event(id)
    return JSONResponse(status_code=200, content={"message": "Se ha eliminado el evento."})

@event_router.get('/events/name/{name}', tags=['eventos'], response_model=Events)
def get_event_by_name(name: str) -> Events:
    db = Session()
    result = EventService(db).get_event_by_name(name)
    if not result:
        return JSONResponse(status_code=404, content={'message': "No encontrado"})
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@event_router.get('/events/description/{description}', tags=['eventos'], response_model=Events)
def get_event_by_description(description:str) -> Events:
    db = Session()
    result = EventService(db).get_event_by_description(description)
    if not result:
        return JSONResponse(status_code=404, content={'message': "No encontrado"})
    return JSONResponse(status_code=200, content=jsonable_encoder(result))