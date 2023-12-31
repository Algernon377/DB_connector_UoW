from DataBaseApi.DB.repositories.base_repository import AbstractRepository
from logger.logger_bot import logger


class BaseService:
    def __init__(self, repository: AbstractRepository):
        self.repository: AbstractRepository = repository

    async def get_all(self):
        rows = await self.repository.find_all()
        return rows

    async def find_many(self, filters):
        try:
            filters = filters.filters_dict
        except Exception as ex:
            logger.error(f'Функция find_many в слое service. Ошибка получения данных \n{ex}\n')
            raise ValueError(f"func find_many in service. Error get data in schema \n{ex}\n")
        rows = await self.repository.find_many(filters)
        return rows
