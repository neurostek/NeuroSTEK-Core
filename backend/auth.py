from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional
import sqlite3
from backend.database import get_connection

router = APIRouter()

class RegisterRequest(BaseModel):
    username: str
    password: str
    email: Optional[str] = None
    gender: Optional[str] = None
    birth_date: Optional[str] = None

@router.post("/register")
def register_user(req: RegisterRequest):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("""
            INSERT INTO users (username, password, email, gender, birth_date)
            VALUES (?, ?, ?, ?, ?)
        """, (req.username, req.password, req.email, req.gender, req.birth_date))
        conn.commit()
    except sqlite3.IntegrityError:
        raise HTTPException(status_code=400, detail="Пользователь уже существует")
    finally:
        conn.close()

    return {"message": "Регистрация успешна", "tokens": 200}

@router.post("/login")
def login_user(req: RegisterRequest):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT password FROM users WHERE username = ?", (req.username,))
    result = cursor.fetchone()
    conn.close()

    if not result or result[0] != req.password:
        raise HTTPException(status_code=401, detail="Неверный логин или пароль")

    return {"message": "Вход выполнен", "username": req.username}
