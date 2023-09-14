from DataBaseApi.DB.models.base_model import Base
from DataBaseApi.DB.schemas.users_schemas import UsersSchema
from sqlalchemy import String, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from typing import Optional


class UsersModel(Base):
    """
    Класс для таблицы users
    При добавлении новго столбца обязательно анатируем, на этом завязано извлечение списка всех столбцов
    Если анотировать необходимо что-то помимо столбца, необходимо переписать логику извлечения имен столбцов
    """
    __tablename__ = 'users'
    user_id: Mapped[str] = mapped_column(nullable=False)
    username: Mapped[Optional[str]] = mapped_column(String(250))
    city: Mapped[Optional[str]] = mapped_column(String(100))
    date_registration: Mapped[Optional[DateTime]] = mapped_column(DateTime(timezone=True), server_default=func.now())
    role: Mapped[Optional[str]] = mapped_column(String(200))

    def to_read_model(self) -> UsersSchema:
        return UsersSchema(
            id=self.id,
            user_id=self.user_id,
            username=self.username,
            city=self.city,
            date_registration=self.date_registration,
            role=self.role,
        )
