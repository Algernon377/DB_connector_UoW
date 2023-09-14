import asyncio
import os
from dotenv import load_dotenv


from sqlalchemy import select

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from DataBaseApi.DB.models.base_model import Base
from DataBaseApi.DB.models.models_list import all_table_dict

from logger.logger_bot import logger


load_dotenv()
POSTGRESQL_URL_FOR_ENGINE = os.getenv('POSTGRESQL_URL_FOR_ENGINE')

engine = create_async_engine(POSTGRESQL_URL_FOR_ENGINE, echo=True, future=True)
async_session_maker = async_sessionmaker(
                                        engine,
                                        expire_on_commit=False,
                                        class_=AsyncSession,
                                        )


async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)



