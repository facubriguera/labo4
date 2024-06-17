from config.database import Base
from sqlalchemy import Column, Integer, String, Enum, Date, ForeignKey

class Events(Base):
    __tablename__ = "events"
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    description = Column(String(200))
    fecha_inicrio = Column(Date)
    fecha_fin = Column(Date)
    lugar = Column(String(50))
    cupos = Column(Integer)
    categoria_id = Column(Integer, ForeignKey)