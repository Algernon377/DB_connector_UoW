from DataBaseApi.DB.utils.repository import AbstractRepository


class BaseService:
    def __init__(self, repository: AbstractRepository):
        self.repository: AbstractRepository = repository


    async def get(self):
        rows = await self.repository.find_all()
        return rows