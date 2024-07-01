from pydantic import BaseModel, Field
from datetime import date


class InscripcionSchema(BaseModel):
    inscrip_id: int = Field (gt=0)
    event_id: int = Field (gt=0)
    user_id: int = Field (gt=0)
    fecha_inscripcion: date

