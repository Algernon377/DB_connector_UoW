from DataBaseApi.DB.schemas.stop_work_schemas import StopWorkAddSchema, StopWorkAddManySchema, StopWorkUpdateSchema
from DataBaseApi.DB.services.base_service import BaseService
from DataBaseApi.DB.models.stop_work_model import StopWorkModel


class StopWorkService(BaseService):

    async def add_one(self, stop_work_data: StopWorkAddSchema):
        stop_work_dict = stop_work_data.model_dump()
        stop_work_obj = StopWorkModel(**stop_work_dict)
        await self.repository.add_one(stop_work_obj)
        return stop_work_obj

    async def add_many(self, list_stop_work_data: StopWorkAddManySchema):
        stop_work_list = [StopWorkModel(**_.model_dump()) for _ in list_stop_work_data.list_obj]
        await self.repository.add_many(stop_work_list)
        return stop_work_list

    async def update(self, list_stop_work_data: StopWorkUpdateSchema):
        filters = list_stop_work_data.filters
        update_data = list_stop_work_data.value
        response_db = await self.repository.update(update_data, filters)
        return response_db


