from DataBaseApi.DB.models.users_model import UsersModel
from DataBaseApi.DB.schemas.users_schemas import UsersAddSchema, UsersAddManySchema, UsersUpdateSchema
from DataBaseApi.DB.services.base_service import BaseService
from logger.logger_bot import logger


class UsersService(BaseService):

    async def add_one(self, user_data: UsersAddSchema) -> UsersModel | bool:
        """
        Добавляет объект в БД
        :param user_data:
        :return: Возвращает или объект модели или False
        """
        try:
            users_dict = user_data.model_dump()
            users_obj = UsersModel(**users_dict)
        except Exception as ex:
            logger.error(f'Функция add_one в слое service. Ошибка получения данных \n{ex}\n')
            raise ValueError(f"func add_one in service. Error get data in schema \n{ex}\n")

        await self.repository.add_one(users_obj)
        return users_obj


    async def add_many(self, list_users_data: UsersAddManySchema) -> list[UsersModel] | bool:
        """
        Добавляет объекты в БД
        :param list_users_data: list с объектами модели
        :return: Возвращает или список объектов модели или False
        """
        try:
            users_list = [UsersModel(**_.model_dump()) for _ in list_users_data.list_obj]
        except Exception as ex:
            logger.error(f'Функция add_many в слое service. Ошибка получения данных \n{ex}\n')
            raise ValueError(f"func add_many in service. Error get data in schema \n{ex}\n")

        await self.repository.add_many(users_list)
        return users_list

    async def update(self, list_users_data: UsersUpdateSchema) -> list | bool:
        """
        Обновляет объекты в БД
        :param list_users_data:
        :return: Возвращает список с кортежами id который обновлялись [(<id>,), (<id>,)] False в случае ошибки
        """
        try:
            filters = list_users_data.filters
            update_data = list_users_data.value
        except Exception as ex:
            logger.error(f'Функция update в слое service. Ошибка получения данных \n{ex}\n')
            raise ValueError(f"func update in service. Error get data in schema \n{ex}\n")

        response_db = await self.repository.update(update_data, filters)
        return response_db
