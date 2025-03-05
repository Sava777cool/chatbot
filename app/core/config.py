from pathlib import Path
from pydantic_settings import BaseSettings

BASE_DIR = Path(__file__).parents[2]


class Settings(BaseSettings):
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    OPENAI_API_KEY: str
    DATABASE_URL: str

    class Config:
        env_file = BASE_DIR / ".env"


settings = Settings()

TORTOISE_ORM = {
    "connections": {"default": settings.DATABASE_URL},
    "apps": {
        "models": {
            "models": ["app.models.user", "app.models.chat", "aerich.models"],
            "default_connection": "default",
        },
    },
}
