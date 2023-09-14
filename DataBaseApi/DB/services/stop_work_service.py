from DataBaseApi.DB.schemas.stop_work_schemas import StopWorkAddSchema
from DataBaseApi.DB.services.base_service import BaseService


class StopWorkService(BaseService):

    async def add(self, stop_work_data: StopWorkAddSchema):
        stop_work_dict = stop_work_data.model_dump()
        stop_work_id = await self.repository.add_one(stop_work_dict)
        return stop_work_id
