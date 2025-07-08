from typing import TypeVar, Generic, Annotated
from pydantic import BaseModel
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.future import select
from sqlalchemy import delete as sqlalchemy_delete, func, Integer
from loguru import logger
from sqlalchemy.ext.asyncio import AsyncSession, AsyncAttrs
from sqlalchemy.orm import mapped_column, Mapped, DeclarativeBase, declared_attr


intpk = Annotated[int, mapped_column(Integer, primary_key=True, autoincrement=True)]


class Base(AsyncAttrs, DeclarativeBase):
    __abstract__ = True

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return f"{cls.__name__.lower()}s"

    id: Mapped[intpk]
