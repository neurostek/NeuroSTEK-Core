from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional

router = APIRouter()

# Временное хранилище пользователей
users_db = {}

class RegisterRequest(BaseModel):
    username: str
    password: str
    email: Optional[str] = None
    gender: Optional[str] = None
    birth_date: Optional[str] = None

@router.post("/register")
def register_user(req: RegisterRequest):
    if req.username in users_db:
        raise HTTPException(status_code=400, detail="Пользователь уже существует")
    
    users_db[req.username] = {
        "password": req.password,
        "email": req.email,
        "gender": req.gender,
        "birth_date": req.birth_date,
        "tokens": 200,
    }
    return {"message": "Регистрация успешна", "tokens": 200}

@router.post("/login")
def login_user(req: RegisterRequest):
    user = users_db.get(req.username)
    if not user or user["password"] != req.password:
        raise HTTPException(status_code=401, detail="Неверный логин или пароль")
    return {"message": "Вход выполнен", "username": req.username}
