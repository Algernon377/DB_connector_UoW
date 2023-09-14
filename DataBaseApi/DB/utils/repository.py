from abc import ABC, abstractmethod

from DataBaseApi.DB.DB_manager import async_session_maker
from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession


class AbstractRepository(ABC):

    @abstractmethod
    async def add_one(self):
        raise NotImplementedError

    @abstractmethod
    async def find_all(self):
        raise NotImplementedError


class SQLAlchemyRepository(AbstractRepository):
    model = None
    def __init__(self, session: AsyncSession):
        self.session = session


    async def add_one(self, values: dict):
        # async with async_session_maker() as session:
        stmt = insert(self.model).values(**values).returning(self.model.id)
        res = await self.session.execute(stmt)
        # await session.commit()
        return res.scalar_one()


    async def find_all(self):
        async with async_session_maker() as session:
            stmt = select(self.model)
            res = await session.execute(stmt)
            res = [row[0].to_read_model() for row in res.all()]
            return res


