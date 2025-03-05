import asyncio
from tortoise import Tortoise, run_async
from app.core.config import settings


async def init():
    await Tortoise.init(
        db_url=settings.DATABASE_URL,
        modules={"models": ["app.models.user", "app.models.chat"]},
    )
    await Tortoise.generate_schemas()


run_async(init())
