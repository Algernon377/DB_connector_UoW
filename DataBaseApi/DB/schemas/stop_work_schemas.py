import datetime

from pydantic import BaseModel
from typing import Optional, Dict, Tuple, List


class StopWorkSchema(BaseModel):
    id: int
    city: str
    object: str
    position: str
    queue: str
    number_bk: str
    cause_stop: str
    cause_info: Optional[str] = None
    user_id_stop_work: str
    user_id_continued_work: Optional[str] = None
    time_stop_work: Optional[datetime.datetime] = None
    time_continued_work: Optional[datetime.datetime] = None
    total_time_not_work: Optional[int] = None
    note: Optional[str] = None

    class Config:
        from_attributes = True

class StopWorkGetSchema(BaseModel):
    filters_dict: Dict


class StopWorkAddSchema(BaseModel):
    city: str
    object: str
    position: str
    queue: str
    number_bk: str
    cause_stop: str
    cause_info: Optional[str] = None
    user_id_stop_work: str
    user_id_continued_work: Optional[str] = None
    time_continued_work: Optional[datetime.datetime] = None
    total_time_not_work: Optional[int] = None
    note: Optional[str] = None

class StopWorkAddManySchema(BaseModel):
    list_obj: List[StopWorkAddSchema]


class StopWorkUpdateSchema(BaseModel):
    value: Dict
    filters: Optional[Dict] = None





class StopWorkPostResponse(BaseModel):
    response_by_db: int | bool

class StopWorkPostManyResponse(BaseModel):
    response_by_db: list | bool


class StopWorkGetResponse(BaseModel):
    response_by_db: List[Tuple] | bool

class StopWorkPutResponse(BaseModel):
    response_by_db: Dict | bool

