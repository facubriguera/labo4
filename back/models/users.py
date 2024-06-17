from config.database import Base
from sqlalchemy import Column, Integer, String, Enum

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    email = Column(String(120), unique=True)
    password = Column(String(40))
    rol = Column(Enum("Cliente", "Administrador", name="user_roles"))