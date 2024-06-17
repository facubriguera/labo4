from config.database import Base
from sqlalchemy import Column, Integer, String, Enum

class Category(Base):
    __tablename__ = "categories"
    cat_id = Column(Integer, primary_key=True)
    nombre = Column(String(50), unique=True)
    descripcion = Column(String(100))