from DataBaseApi.DB.repositories.base_repository import AbstractRepository


class BaseService:
    def __init__(self, repository: AbstractRepository):
        self.repository: AbstractRepository = repository

    async def get_all(self):
        rows = await self.repository.find_all()
        return rows

    async def find_many(self, filters):
        rows = await self.repository.find_many(filters)
        return rows
