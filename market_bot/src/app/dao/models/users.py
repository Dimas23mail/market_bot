import datetime
from typing import Optional

from sqlalchemy import text, ForeignKey, PickleType, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.dao.base import Base


class User(Base):
    __tablename__ = "users"

    user_name: Mapped[Optional[str]] = mapped_column(String(20))
    telegram_id: Mapped[int] = mapped_column(unique=True)
    created_at: Mapped[datetime.datetime] = mapped_column(
        server_default=text("TIMEZONE('utc', now())"),
        default=datetime.UTC
    )
    updated_at: Mapped[datetime.datetime] = mapped_column(
        server_default=text("TIMEZONE('utc', now())"),
        default=datetime.UTC
    )


class UserHistory(Base):
    __tablename__ = "users_history"

    created_at: Mapped[datetime.datetime] = mapped_column(
        server_default=text("TIMEZONE('utc', now())"), default=datetime.UTC
    )
    updated_at: Mapped[datetime.datetime] = mapped_column(
        server_default=text("TIMEZONE('utc', now())"),
        default=datetime.UTC,
        onupdate=datetime.UTC,
    )
    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"), server_default=text("1")
    )
    request_history: Mapped[str]
    order_history: Mapped[str]
