from typing import Any

from sqlalchemy import ForeignKey, String, BigInteger
from sqlalchemy.orm import Mapped, DeclarativeBase, mapped_column
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine


def create_and_connect_to_db() -> bool | Any:
    engine = create_async_engine(url='sqlite+aiosqlite:///market_db.sqlite3', echo=True)
    return engine


async def make(engine: None) -> bool | Any:
    if engine:
        async_session = async_sessionmaker(bind=engine, expire_on_commit=False)
        return async_session
    else:
        return False


class Base(AsyncAttrs, DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    tg_id = mapped_column(BigInteger)


class History(Base):
    __tablename__ = 'history_table'

    id: Mapped[int] = mapped_column(primary_key=True)
    user: Mapped[int] = mapped_column(ForeignKey('users.id', ondelete='CASCADE'))


class Product(Base):
    __tablename__ = 'product_list'

    id: Mapped[int] = mapped_column(primary_key=True)
    title = mapped_column(String(128))
    price: Mapped[int] = mapped_column()
    mainImageURL = mapped_column(String(128))
    description = mapped_column(String(250))
    availability: Mapped[int] = mapped_column(default=0)
    allImagesListUrl = mapped_column(String(250))
    color = mapped_column(String(50))
    room = mapped_column(String(50))


async def init_db():
    engine = create_and_connect_to_db
    if engine:
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
