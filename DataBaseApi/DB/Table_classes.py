from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func


Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'

    user_id = Column(String(50), primary_key=True)
    username = Column(String(250))
    city = Column(String(100))
    date_registration = Column(DateTime(timezone=True), server_default=func.now())
    role = Column(String(200))

    stop_work = relationship("StopWork")


class StopWork(Base):
    __tablename__ = 'stop_work'

    id = Column(Integer, primary_key=True, autoincrement=True)
    city = Column(String(100))
    object = Column(String(200))
    number_bk = Column(String(100))
    cause_stop = Column(String(200))
    info_cause = Column(String(200))
    user_id_stop_work = Column(String(50), ForeignKey('users.user_id'))
    user_id_continued_work = Column(String(50), ForeignKey('users.user_id'))
    time_stop_work = Column(DateTime)
    time_continued_work = Column(DateTime)
    total_time_not_work = Column(DateTime)
    note = Column(String)

    users = relationship("Users")










