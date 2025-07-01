from fastapi import APIRouter, HTTPException
import sqlite3
from backend.database import get_connection

router = APIRouter()

@router.get("/balance/{username}")
def get_balance(username: str):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT tokens FROM users WHERE username = ?", (username,))
    result = cursor.fetchone()
    conn.close()

    if not result:
        raise HTTPException(status_code=404, detail="Пользователь не найден")

    return {"tokens": result[0]}

@router.post("/spend/{username}")
def spend_tokens(username: str, amount: int):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT tokens FROM users WHERE username = ?", (username,))
    result = cursor.fetchone()

    if not result or result[0] < amount:
        conn.close()
        raise HTTPException(status_code=400, detail="Недостаточно токенов")

    new_balance = result[0] - amount
    cursor.execute("UPDATE users SET tokens = ? WHERE username = ?", (new_balance, username))
    conn.commit()
    conn.close()

    return {"message": "Списано", "remaining": new_balance}

@router.post("/reward/{username}")
def reward_tokens(username: str, amount: int):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT tokens FROM users WHERE username = ?", (username,))
    result = cursor.fetchone()

    if not result:
        conn.close()
        raise HTTPException(status_code=404, detail="Пользователь не найден")

    new_balance = result[0] + amount
    cursor.execute("UPDATE users SET tokens = ? WHERE username = ?", (new_balance, username))
    conn.commit()
    conn.close()

    return {"message": "Начислено", "new_balance": new_balance}
