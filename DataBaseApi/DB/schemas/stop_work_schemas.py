import datetime

from pydantic import BaseModel
from typing import Optional


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

