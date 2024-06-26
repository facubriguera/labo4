from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.ext.declarative import declarative_base
from config.database import Base

Base = declarative_base()

class UserModel(Base):
    __tablename__ = "users"
    user_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    email = Column(String(120), unique=True)
    password = Column(String(40))
    rol = Column(Enum("Cliente", "Administrador", name="user_roles"))
