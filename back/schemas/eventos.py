from pydantic import BaseModel
from datetime import date

class Events(BaseModel):
    event_id: int
    name: str
    description: str
    fecha_inicio: date
    fecha_fin: date
    lugar: str
    cupos: int
    cat_id: int