from DataBaseApi.DB.utils.repository import SQLAlchemyRepository
from DataBaseApi.DB.models.users_model import UsersModel


class UsersRepository(SQLAlchemyRepository):
    model = UsersModel
