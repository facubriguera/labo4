from pydantic import BaseModel, EmailStr 
from typing import List, Optional 
from datetime import date;

class InscriptionBase(BaseModel):
    id : int
    eventID : int
    userID: int
    date_insc : date

class InscriptionCreate(InscriptionBase):
    pass

class InscriptionHistory(InscriptionBase):
    id: int
    class Config:
        orm_mode = True