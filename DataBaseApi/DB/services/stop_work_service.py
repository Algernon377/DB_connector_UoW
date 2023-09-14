from DataBaseApi.DB.schemas.stop_work_schemas import StopWorkAddSchema, StopWorkAddManySchema, StopWorkUpdateSchema
from DataBaseApi.DB.services.base_service import BaseService
from DataBaseApi.DB.models.stop_work_model import StopWorkModel
from logger.logger_bot import logger


class StopWorkService(BaseService):

    async def add_one(self, stop_work_data: StopWorkAddSchema):
        try:
            stop_work_dict = stop_work_data.model_dump()
            stop_work_obj = StopWorkModel(**stop_work_dict)
        except Exception as ex:
            logger.error(f'Функция add_one в слое service. Ошибка получения данных \n{ex}\n')
            return False

        resp = await self.repository.add_one(stop_work_obj)
        if resp:
            return stop_work_obj
        return False

    async def add_many(self, list_stop_work_data: StopWorkAddManySchema):
        try:
            stop_work_list = [StopWorkModel(**_.model_dump()) for _ in list_stop_work_data.list_obj]
        except Exception as ex:
            logger.error(f'Функция add_many в слое service. Ошибка получения данных \n{ex}\n')
            return False

        resp = await self.repository.add_many(stop_work_list)
        if resp:
            return stop_work_list
        return False


    async def update(self, list_stop_work_data: StopWorkUpdateSchema):
        try:
            filters = list_stop_work_data.filters
            update_data = list_stop_work_data.value
        except Exception as ex:
            logger.error(f'Функция update в слое service. Ошибка получения данных \n{ex}\n')
            return False

        response_db = await self.repository.update(update_data, filters)
        return response_db


