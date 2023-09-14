from DataBaseApi.DB.repositories.base_repository import SQLAlchemyRepository
from DataBaseApi.DB.models.stop_work_model import StopWorkModel


class StopWorkRepository(SQLAlchemyRepository):
    model = StopWorkModel
