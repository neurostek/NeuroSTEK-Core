from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional
from ai_core.history import add_to_history, get_last_messages

router = APIRouter()

class Message(BaseModel):
    username: str
    message: str

@router.post("/chat")
def chat_with_ai(data: Message):
    # Временно: заглушка ответа от AI
    user_msg = data.message
    username = data.username

    # Сохраняем в историю
    add_to_history(username, "user", user_msg)

    # Генерируем ответ
    if "привет" in user_msg.lower():
        bot_reply = "Приветствую тебя, друг! Чем могу помочь?"
    else:
        bot_reply = "Это тестовый ответ AI. Скоро я стану умнее 😎"

    # Сохраняем ответ бота
    add_to_history(username, "bot", bot_reply)

    return {"reply": bot_reply}
