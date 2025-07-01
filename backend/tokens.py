from fastapi import APIRouter, HTTPException
from typing import Dict

router = APIRouter()

# Используем ту же базу пользователей
from backend.auth import users_db

@router.get("/balance/{username}")
def get_balance(username: str):
    user = users_db.get(username)
    if not user:
        raise HTTPException(status_code=404, detail="Пользователь не найден")
    return {"tokens": user.get("tokens", 0)}

@router.post("/spend/{username}")
def spend_tokens(username: str, amount: int):
    user = users_db.get(username)
    if not user or user["tokens"] < amount:
        raise HTTPException(status_code=400, detail="Недостаточно токенов")
    user["tokens"] -= amount
    return {"message": "Списано", "remaining": user["tokens"]}

@router.post("/reward/{username}")
def reward_tokens(username: str, amount: int):
    user = users_db.get(username)
    if not user:
        raise HTTPException(status_code=404, detail="Пользователь не найден")
    user["tokens"] += amount
    return {"message": "Начислено", "new_balance": user["tokens"]}
