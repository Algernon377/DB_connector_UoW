from DataBaseApi.DB.schemas.users_schemas import UsersAddSchema
from DataBaseApi.DB.services.base_service import BaseService


class UsersService(BaseService):

    async def add(self, user_data: UsersAddSchema):
        users_dict = user_data.model_dump()
        user_id = await self.repository.add_one(users_dict)
        return user_id
