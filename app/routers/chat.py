import openai
from fastapi import APIRouter, Depends
from app.models.chat import ChatHistory
from app.schemas.chat import ChatRequest, ChatResponse
from app.core.config import settings

router = APIRouter()

openai.api_key = settings.OPENAI_API_KEY


@router.post("/send", response_model=ChatResponse)
async def send_message(chat_data: ChatRequest):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=[{"role": "user", "content": chat_data.message}]
    )
    chat_response = response["choices"][0]["message"]["content"]

    await ChatHistory.create(
        user=chat_data.user_id, message=chat_data.message, response=chat_response
    )

    return {"message": chat_data.message, "response": chat_response}


@router.get("/history")
async def chat_history(user_id: int):
    chats = await ChatHistory.filter(user=user_id).values(
        "message", "response", "timestamp"
    )
    return {"history": chats}
