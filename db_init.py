from tortoise import Tortoise, fields
from tortoise.models import Model
from app.core.config import settings


async def init_db():
    await Tortoise.init(
        db_url=settings.DATABASE_URL,
        modules={
            "models": ["app.models.user", "app.models.chat", "aerich.models"],
            "default_connection": "default",
        },
    )
    await Tortoise.generate_schemas()
