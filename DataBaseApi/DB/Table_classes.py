from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from typing import Optional
from typing import List
from datetime import datetime
import inspect
import sys

class Base(DeclarativeBase):
    pass


class UsersTable(Base):
    '''
    Класс для таблицы users
    При добавлении новго столбца обязательно анатируем, на этом завязано извлечение списка всех столбцов
    Если анотировать необходимо что-то по мимо столбца, необходимо переписать логику извлечения имен столбцов
    '''
    __tablename__ = 'users'

    user_id: Mapped[str] = mapped_column(primary_key=True, nullable=False)
    username: Mapped[Optional[str]] = mapped_column(String(250))
    city: Mapped[Optional[str]] = mapped_column(String(100))
    date_registration: Mapped[DateTime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    role: Mapped[Optional[str]]= mapped_column(String(200))

    stop_work = relationship("StopWorkTable", back_populates="users", overlaps="stop_work")

    # def __repr__(self) -> str:
    #     return f"User(id={self.user_id}, username={self.username}, city={self.city},date_registration={self.date_registration}, role={self.role})"

class StopWorkTable(Base):
    '''
    Класс для таблицы stop_work
    При добавлении новго столбца обязательно анатируем, на этом завязано извлечение списка всех столбцов
    Если анотировать необходимо что-то по мимо столбца, необходимо переписать логику извлечения имен столбцов
    '''
    __tablename__ = 'stop_work'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    city: Mapped[str]= mapped_column(String(100))
    object: Mapped[str] = mapped_column(String(200))
    number_bk: Mapped[str] = mapped_column(String(100))
    cause_stop: Mapped[str] = mapped_column(String(200))
    info_cause: Mapped[Optional[str]] = mapped_column(String(200))
    user_id_stop_work: Mapped[str] = mapped_column(String(50), ForeignKey('users.user_id'))
    user_id_continued_work: Mapped[str] = mapped_column(String(50))
    time_stop_work: Mapped[datetime]
    time_continued_work: Mapped[datetime]
    total_time_not_work: Mapped[datetime]
    note: Mapped[str]

    users = relationship("UsersTable", back_populates="stop_work", overlaps="stop_work")



all_table_dict = {
    UsersTable.__tablename__: UsersTable,
    StopWorkTable.__tablename__: StopWorkTable
}





