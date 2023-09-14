from DataBaseApi.DB.models.users_model import UsersModel
from DataBaseApi.DB.schemas.users_schemas import UsersAddSchema, UsersAddManySchema, UsersUpdateSchema
from DataBaseApi.DB.services.base_service import BaseService


class UsersService(BaseService):

    async def add_one(self, user_data: UsersAddSchema):
        users_dict = user_data.model_dump()
        user_id = await self.repository.add_one(users_dict)
        return user_id

    async def add_many(self, list_stop_work_data: UsersAddManySchema):
        stop_work_list = [UsersModel(**stop_work_data.model_dump()) for stop_work_data in list_stop_work_data.list_obj]
        await self.repository.add_many(stop_work_list)
        return stop_work_list

    async def update(self, list_stop_work_data: UsersUpdateSchema):
        filters = list_stop_work_data.filters
        update_data = list_stop_work_data.value
        response_db = await self.repository.update(update_data, filters)
        return response_db
