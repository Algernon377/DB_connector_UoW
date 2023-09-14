from enum import Enum
from typing import Optional, Dict, Tuple, List
from pydantic import BaseModel

from ..DB.models.models_list import all_table_dict


#request Class
TableName = Enum("TableName", {table: table for table in all_table_dict})


class RequestGet(BaseModel):
    name_columns_tuple: Tuple
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












