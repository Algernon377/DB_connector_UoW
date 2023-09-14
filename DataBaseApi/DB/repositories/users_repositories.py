from DataBaseApi.DB.repositories.base_repository import SQLAlchemyRepository
from DataBaseApi.DB.models.users_model import UsersModel


class UsersRepository(SQLAlchemyRepository):
    model = UsersModel
