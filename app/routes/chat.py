import openai
from fastapi import APIRouter
from app.models.chat import ChatHistory
from app.schemas.chat import ChatRequest, ChatResponse, ChatHistoryResponse
from app.core.config import settings

router = APIRouter()

openai.api_key = settings.OPENAI_API_KEY


@router.post("/send", response_model=ChatResponse)
async def send_message(chat_data: ChatRequest):
    try:
        response = await openai.ChatCompletion.acreate(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": chat_data.message}],
        )
        chat_response = response["choices"][0]["message"]["content"]

        await ChatHistory.create(
            user_id=chat_data.user_id, message=chat_data.message, response=chat_response
        )

        return ChatResponse(message=chat_data.message, response=chat_response)

    except Exception as e:
        raise e


@router.get("/history", response_model=ChatHistoryResponse)
async def chat_history(user_id: int):
    chats = await ChatHistory.filter(user_id=user_id).values(
        "message", "response", "created_at"
    )
    return {"history": chats}
