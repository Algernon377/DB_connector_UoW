from DataBaseApi.DB.models.stop_work_model import StopWorkModel
from DataBaseApi.DB.models.users_model import UsersModel

all_table_dict = {
    UsersModel.__tablename__: UsersModel,
    StopWorkModel.__tablename__: StopWorkModel
}
