from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List, Literal
from pydantic import BaseModel, EmailStr

from config.database import Session  # Asegúrate de importar SessionLocal desde config.database
from models.users import UserModel as UserModel  # Importa el modelo de usuario correcto
from services.userServices import UserService

user_router = APIRouter()

def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()

class User(BaseModel):
    id: int
    name: str
    email: EmailStr
    password: str
    rol: Literal["Cliente", "Administrador"]

class UserCreate(BaseModel):
#    id: int
    name: str
    email: EmailStr
    password: str
    rol: Literal["Cliente", "Administrador"]

class UserUpdate(BaseModel):
    name: str = None
    email: EmailStr = None
    password: str = None
    rol: str = None

@user_router.get('/users', response_model=List[User], tags=['Usuarios'])
def get_users(db: Session = Depends(get_db)):
    return UserService(db).get_users()

@user_router.get('/users/{user_id}', response_model=User, tags=['Usuarios'])
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = UserService(db).get_user(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return user

@user_router.post('/users', response_model=User, status_code=201, tags=['Usuarios'])
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return UserService(db).create_user(user)

@user_router.put('/users/{user_id}', response_model=User, tags=['Usuarios'])
def update_user(user_id: int, user: UserUpdate, db: Session = Depends(get_db)):
    return UserService(db).update_user(user_id, user)

@user_router.delete('/users/{user_id}', response_model=dict, tags=['Usuarios'])
def delete_user(user_id: int, db: Session = Depends(get_db)):
    return UserService(db).delete_user(user_id)
