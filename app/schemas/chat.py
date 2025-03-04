from pydantic import BaseModel
from datetime import datetime


class ChatRequest(BaseModel):
    """Schema request for sending a message to the bot"""

    user_id: int
    message: str


class ChatResponse(BaseModel):
    """Schema response from the bot"""

    message: str
    response: str


class ChatHistoryItem(BaseModel):
    """Schema for chat history item"""

    message: str
    response: str
    timestamp: datetime


class ChatHistoryResponse(BaseModel):
    """Schema for chat history response"""

    history: list[ChatHistoryItem]
