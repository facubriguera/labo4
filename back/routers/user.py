from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from utils.jwt_manager import create_token
from fastapi.responses import JSONResponse
from schemas.users import User

user_router = APIRouter()

@user_router.post('/login', tags=['auth'])
def login(user: User):
    #Si está bien la pass y user nos da el token, caso contrario usamos else y devolvemos un texto de
    #credenciales invalidas siu xd 
    if user.email == "admin@gmail.com" and user.password == "admin":
        token = create_token(user.dict())
        return JSONResponse(status_code=200, content={"token": token})
    else:
        raise HTTPException(status_code=401, detail="Credenciales inválidas")

