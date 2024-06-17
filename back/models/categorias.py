from pydantic import BaseModel, EmailStr
from typing import List, Optional

class Category(BaseModel):
    id : int
    nombre : str
    descripcion : str
