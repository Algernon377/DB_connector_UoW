from DataBaseApi.DB.models.users_model import UsersModel
from DataBaseApi.DB.schemas.users_schemas import UsersAddSchema, UsersAddManySchema, UsersUpdateSchema
from DataBaseApi.DB.services.base_service import BaseService
from logger.logger_bot import logger


class UsersService(BaseService):

    async def add_one(self, user_data: UsersAddSchema):
        try:
            users_dict = user_data.model_dump()
        except Exception as ex:
            logger.error(f'Функция add_one в слое service. Ошибка получения данных \n{ex}\n')
            return False

        user_id = await self.repository.add_one(users_dict)
        if user_id:
            return user_id
        return False

    async def add_many(self, list_users_data: UsersAddManySchema):
        try:
            users_list = [UsersModel(**_.model_dump()) for _ in list_users_data.list_obj]
        except Exception as ex:
            logger.error(f'Функция add_many в слое service. Ошибка получения данных \n{ex}\n')
            return False

        resp = await self.repository.add_many(users_list)
        if resp:
            return users_list
        return False

    async def update(self, list_users_data: UsersUpdateSchema):
        try:
            filters = list_users_data.filters
            update_data = list_users_data.value
        except Exception as ex:
            logger.error(f'Функция update в слое service. Ошибка получения данных \n{ex}\n')
            return False

        response_db = await self.repository.update(update_data, filters)
        return response_db
