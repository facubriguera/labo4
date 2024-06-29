from pydantic import BaseModel, EmailStr
from typing import List, Optional

class Category(BaseModel):
    cat_id : int
    nombre : str
    descripcion : str

    