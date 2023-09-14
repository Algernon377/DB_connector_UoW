import datetime
from typing import Optional

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

class UsersAddSchema(BaseModel):
    user_id: str
    username: Optional[str] = None
    city: Optional[str] = None
    role: Optional[str] = None