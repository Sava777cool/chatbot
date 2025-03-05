from fastapi import APIRouter, HTTPException
from datetime import timedelta
from app.models.user import User
from app.schemas.user import UserCreate, Token
from app.core.security import hash_password, verify_password, create_access_token
from app.core.config import settings
from tortoise.transactions import in_transaction

router = APIRouter()


@router.post("/register", response_model=Token)
async def register(user_data: UserCreate):
    async with in_transaction():
        user = await User.create(
            username=user_data.username, password_hash=hash_password(user_data.password)
        )
    access_token = create_access_token(
        data={"sub": user.username},
        expires_delta=timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES),
    )
    return {"access_token": access_token, "token_type": "bearer"}


@router.post("/login", response_model=Token)
async def login(user_data: UserCreate):
    user = await User.get_or_none(username=user_data.username)
    if not user or not verify_password(user_data.password, user.password_hash):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    access_token = create_access_token(
        data={"sub": user.username},
        expires_delta=timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES),
    )
    return {"access_token": access_token, "token_type": "bearer"}
