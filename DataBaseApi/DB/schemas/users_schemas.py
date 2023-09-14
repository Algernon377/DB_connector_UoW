import datetime
from typing import Optional, Dict, Tuple, List

from pydantic import BaseModel


class UsersSchema(BaseModel):
    id: int
    user_id: str
    username: Optional[str] = None
    city: Optional[str] = None
    date_registration: datetime.datetime
    role: Optional[str] = None

    class Config:
        from_attributes = True

class UsersGetSchema(BaseModel):
    filters: Dict


class UsersAddSchema(BaseModel):
    user_id: str
    username: Optional[str] = None
    city: Optional[str] = None
    role: Optional[str] = None

class UsersAddManySchema(BaseModel):
    list_obj: List[UsersAddSchema]

class UsersUpdateSchema(BaseModel):
    value: Dict
    filters: Optional[Dict] = None



class UsersPostResponse(BaseModel):
    response_by_db: int | bool

class UsersPostManyResponse(BaseModel):
    response_by_db: list | bool


class UsersGetResponse(BaseModel):
    response_by_db: List[Tuple] | bool

class UsersPutResponse(BaseModel):
    response_by_db: Dict | bool