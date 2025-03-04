from pydantic import BaseModel


class UserCreate(BaseModel):
    """Schema for registering a new user."""

    username: str
    password: str


class Token(BaseModel):
    """Schema for response with access token."""

    access_token: str
    token_type: str


class UserResponse(BaseModel):
    """Schema response with user information."""

    id: int
    username: str

    class Config:
        from_attributes = True
