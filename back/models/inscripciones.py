from pydantic import BaseModel, EmailStr 
from typing import List, Optional 
from datetime import Date;

class Instription(BaseModel):
    id : int
    eventID : int
    userID: int
    date_insc : Date