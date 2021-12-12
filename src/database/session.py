from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine

from src.core import get_settings


engine  = create_async_engine(get_settings().DB_URL)
session = sessionmaker(
    bind = engine,
    class_ = AsyncSession,
    autoflush = True,
    autocommit = False
)

async def get_db() -> AsyncSession:
    async with session() as db:
        try:
            yield db
        finally:
            await db.close() 