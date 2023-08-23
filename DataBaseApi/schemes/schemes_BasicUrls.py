from enum import Enum
from typing import Optional, Dict, Tuple, List
from pydantic import BaseModel

from ..DB.Table_classes import all_table_dict


#request Class
TableName = Enum("TableName", {table: table for table in all_table_dict})


class RequestGet(BaseModel):
    name_columns_tuple: Tuple[str]
    where_dict: Optional[Dict] = None
    limit: Optional[int] = None

class ResponseGet(BaseModel):
    response_by_db: List[Tuple]|bool



class RequestSet(BaseModel):
    set_dict: Dict


class ResponseSet(BaseModel):
    response_by_db: bool


class RequestSetMany(BaseModel):
    set_many_list: List[dict]
    group_write: Optional[bool] = True


class ResponseSetMany(BaseModel):
    response_by_db: bool


class RequestUpdate(BaseModel):
    update_columns_dict: Dict
    where_dict: Optional[Dict] = None


class ResponseUpdate(BaseModel):
    response_by_db: bool
#
# class SetMethod(BaseModel):
#     dict_request: Dict
#
#
# class UpdateMethod(BaseModel):
#     update_dict: Dict
#
#
# class JoinMethod(BaseModel):
#     dict_request: Dict
#     name_data_base_obj_2: str
#     dict_detail_request:  Optional[Dict] = None
#     limit: Optional[int] = None
#
#
# class UpdateManyMethod(BaseModel):
#     dict_where: Dict
#     dict_update: Dict
#
#
# class GetDateMethod(BaseModel):
#     dict_request: Dict
#     name_day: str = 'birthday'
#     range_day: int = 1
#
#
# class CommandExecutorMethod(BaseModel):
#     sql_command: str
#
#
# #response class
# class BasicRespBool(BaseModel):
#     response_by_db: bool = False
#
#
# class BasicRespData(BaseModel):
#     response_by_db: List[Tuple] | bool = False
#
# class BasicRespColumns(BaseModel):
#     response_by_db: Tuple











