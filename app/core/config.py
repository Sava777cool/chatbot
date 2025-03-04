from pathlib import Path
from pydantic_settings import BaseSettings

BASE_DIR = Path(__file__).parents[2]


class Settings(BaseSettings):
    DATABASE_URL: str
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    OPENAI_API_KEY: str

    class Config:
        env_file = BASE_DIR / ".env"


settings = Settings()
