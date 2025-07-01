from fastapi import FastAPI
from backend.auth import router as auth_router
from backend.tokens import router as token_router
from backend.database import init_db  # ← импорт в начале

app = FastAPI(title="NeuroSTEK Backend")

@app.get("/")
def root():
    return {"message": "NeuroSTEK API is running"}

app.include_router(auth_router, prefix="/auth")
app.include_router(token_router, prefix="/tokens")

init_db()  # ← вызов в самом конце
