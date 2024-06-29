from config.database import Base
from sqlalchemy import Column, Integer, String, Date, ForeignKey

class Events(Base):
    __tablename__ = "events"
    event_id = Column(Integer, primary_key=True)
    name = Column(String(50))
    description = Column(String(200))
    fecha_inicio = Column(Date)
    fecha_fin = Column(Date)
    lugar = Column(String(50))
    cupos = Column(Integer)
    cat_id = Column(Integer, ForeignKey("categories.cat_id"))