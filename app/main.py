from fastapi import FastAPI
from app.core.db import init_db, close_db
from app.routes.auth import router as auth_router
from app.routes.chat import router as chat_router

app = FastAPI(title="FastAPI Chatbot")


@app.on_event("startup")
async def startup():
    await init_db()


@app.on_event("shutdown")
async def shutdown():
    await close_db()


app.include_router(auth_router, prefix="/auth", tags=["Auth"])
app.include_router(chat_router, prefix="/chat", tags=["Chat"])
