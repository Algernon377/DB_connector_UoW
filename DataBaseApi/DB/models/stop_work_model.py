import datetime

from DataBaseApi.DB.models.main_base_model import Base
from DataBaseApi.DB.schemas.stop_work_schemas import StopWorkSchema
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from typing import Optional
from sqlalchemy import String, DateTime
from sqlalchemy.sql import func


class StopWorkModel(Base):
    """
    Класс для таблицы stop_work
    При добавлении новго столбца обязательно анатируем, на этом завязано извлечение списка всех столбцов
    Если анотировать необходимо что-то помимо столбца, необходимо переписать логику извлечения имен столбцов
    """
    __tablename__ = 'stop_work'

    city: Mapped[str] = mapped_column(String(100))
    object: Mapped[str] = mapped_column(String(200))
    position: Mapped[str] = mapped_column(String(10))
    queue: Mapped[str] = mapped_column(String(10))
    number_bk: Mapped[str] = mapped_column(String(100))
    cause_stop: Mapped[str] = mapped_column(String(200))
    cause_info: Mapped[Optional[str]] = mapped_column(String(200))
    user_id_stop_work: Mapped[str] = mapped_column(String(50))
    user_id_continued_work: Mapped[Optional[str]] = mapped_column(String(50))
    time_stop_work: Mapped[Optional[DateTime]] = mapped_column(DateTime(timezone=True), server_default=func.now())
    time_continued_work: Mapped[Optional[datetime.datetime]]
    total_time_not_work: Mapped[Optional[int]]
    note: Mapped[Optional[str]]

    def to_read_model(self) -> StopWorkSchema:
        return StopWorkSchema(
            id=self.id,
            city=self.city,
            object=self.object,
            position=self.position,
            queue=self.queue,
            number_bk=self.number_bk,
            cause_stop=self.cause_stop,
            cause_info=self.cause_info,
            user_id_stop_work=self.user_id_stop_work,
            user_id_continued_work=self.user_id_continued_work,
            time_stop_work=self.time_stop_work,
            time_continued_work=self.time_continued_work,
            total_time_not_work=self.total_time_not_work,
            note=self.note,

        )
