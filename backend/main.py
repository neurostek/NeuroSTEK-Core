from fastapi import FastAPI
from backend.auth import router as auth_router
from backend.tokens import router as token_router

app = FastAPI(title="NeuroSTEK Backend")

@app.get("/")
def root():
    return {"message": "NeuroSTEK API is running"}

app.include_router(auth_router, prefix="/auth")
app.include_router(token_router, prefix="/tokens")

from backend.database import init_db

init_db()  # инициализация базы при запуске
