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

inscription_router = APIRouter()

@inscription_router.get('/inscription')
def get_user_inscriptions(self):
    return 

@inscription_router.get('/inscription')
def get_user_incription_history(self):
    return