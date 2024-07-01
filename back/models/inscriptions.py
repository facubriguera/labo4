from config.database import Base
from sqlalchemy import Column, Integer, Date, ForeignKey

class InscripcionModel(Base):
    __tablename__ = "inscriptions"
    inscrip_id = Column(Integer, primary_key=True)
    event_id = Column(Integer, ForeignKey("events.event_id"))
    user_id = Column(Integer, ForeignKey("users.user_id"))
    fecha_inscripcion = Column(Date)