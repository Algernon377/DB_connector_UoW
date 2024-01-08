from DataBaseApi.DB.schemas.stop_work_schemas import StopWorkAddSchema, StopWorkAddManySchema, StopWorkUpdateSchema
from DataBaseApi.DB.services.base_service import BaseService
from DataBaseApi.DB.models.stop_work_model import StopWorkModel
from logger.logger_bot import logger


class StopWorkService(BaseService):

    async def add_one(self, stop_work_data: StopWorkAddSchema) -> StopWorkModel | bool:
        """
        Добавляет объект в БД
        :param stop_work_data:
        :return: Возвращает или объект модели или False
        """
        try:
            stop_work_dict = stop_work_data.model_dump()
            stop_work_obj = StopWorkModel(**stop_work_dict)
        except Exception as ex:
            logger.error(f'Функция add_one в слое service. Ошибка получения данных \n{ex}\n')
            raise ValueError(f"func add_one in service. Error get data in schema \n{ex}\n")

        await self.repository.add_one(stop_work_obj)
        return stop_work_obj


    async def add_many(self, list_stop_work_data: StopWorkAddManySchema) -> list[StopWorkModel] | bool:
        """
        Добавляет объекты в БД
        :param list_stop_work_data: list с объектами модели
        :return: Возвращает или список объектов модели или False
        """
        try:
            stop_work_list = [StopWorkModel(**_.model_dump()) for _ in list_stop_work_data.list_obj]
        except Exception as ex:
            logger.error(f'Функция add_many в слое service. Ошибка получения данных \n{ex}\n')
            raise ValueError(f"func add_many in service. Error get data in schema \n{ex}\n")

        await self.repository.add_many(stop_work_list)
        return stop_work_list

    async def update(self, list_stop_work_data: StopWorkUpdateSchema) -> list | bool:
        """
        Обновляет объекты в БД
        :param list_stop_work_data:
        :return: Возвращает список с кортежами id который обновлялись [(<id>,), (<id>,)] False в случае ошибки
        """
        try:
            filters = list_stop_work_data.filters
            update_data = list_stop_work_data.value
        except Exception as ex:
            logger.error(f'Функция update в слое service. Ошибка получения данных \n{ex}\n')
            raise ValueError(f"func update in service. Error get data in schema \n{ex}\n")

        response_db = await self.repository.update(update_data, filters)
        return response_db


