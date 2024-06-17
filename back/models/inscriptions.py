from config.database import Base
from sqlalchemy import Column, Integer, Date, ForeignKey

class Inscriptions(Base):
    __tablename__ = "inscriptions"
    id = Column(Integer, primary_key=True)
    event_id = Column(Integer, ForeignKey)
    user_id = Column(Integer, ForeignKey)
    fecha_inscripcion = Column(Date)