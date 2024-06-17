from pydantic import BaseModel, EmailStr
from typing import List, Optional

class User(BaseModel):
    id: int
    name: str
    email : EmailStr
    password : str
    rol : str