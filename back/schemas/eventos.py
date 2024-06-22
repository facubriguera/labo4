from pydantic import BaseModel
from datetime import date

class Events(BaseModel):
    id: int
    nombre: str
    descripcion: str
    fecha_inicio: date
    fecha_fin: date
    lugar: str
    cupos: int
    categoria_id: int