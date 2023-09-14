from abc import ABC, abstractmethod


from pydantic import BaseModel
from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession


class AbstractRepository(ABC):

    @abstractmethod
    async def add_one(self, *args):
        raise NotImplementedError

    @abstractmethod
    async def add_many(self, *args):
        raise NotImplementedError

    @abstractmethod
    async def find_all(self, *args):
        raise NotImplementedError

    @abstractmethod
    async def find_many(self, *args):
        raise NotImplementedError

    @abstractmethod
    async def update(self, *args):
        raise NotImplementedError


class SQLAlchemyRepository(AbstractRepository):
    """
    Конкретный класс работы с БД От него наследуются остальные репозитории
    """
    model = None

    def __init__(self, session: AsyncSession):
        self.session = session

    async def add_one(self, values: BaseModel):
        """
        Добавление одной новой записи в БД
        :param values: Объект класса модели БД
        :return:
        """
        self.session.add(values)

    async def add_many(self, values: list):
        """
        Добавление множества значений в БД
        :param values: Список из объектов моделей.
        :return:
        """
        self.session.add_all(values)

    async def update(self, values: dict, filters: dict | None):
        """
        Обновление данных в БД
        :param values: dict с меняемыми значениями {<название столбца>:<новое значение столбца>}
        :param filters: dict с фильтрами {<название столбца>:<значение столбца>}
        :return:
        """
        stmt = update(self.model).values(**values).returning(self.model.id)
        if filters:
            stmt = stmt.filter_by(**filters)
        response_db = await self.session.execute(stmt)
        return response_db.all()

    async def find_all(self):
        """
        Взятие всех значений из БД
        :return:
        """
        stmt = select(self.model)
        res = await self.session.execute(stmt)
        res = [row[0].to_read_model() for row in res.all()]
        return res

    async def find_many(self, filters: dict | None):
        """
        Взятие значений из БД по фильтрам
        :param filters: dict с фильтрами {<название столбца>:<значение столбца>}
        :return:
        """
        stmt = select(self.model)
        if filters:
            stmt = stmt.filter_by(**filters)
        res = await self.session.execute(stmt)
        res = [row[0].to_read_model() for row in res.all()]
        return res
