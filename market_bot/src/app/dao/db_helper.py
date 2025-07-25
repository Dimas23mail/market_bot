from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine, AsyncSession, async_scoped_session
from asyncio import current_task

from app.config import settings


class DataBaseHelper:
    def __init__(self, url: str, echo: bool = False):
        self.engine = create_async_engine(
            url=url,
            echo=echo,  # Only debugging!!!
            pool_size=5,
            max_overflow=10
        )
        self.session_factory = async_sessionmaker(
            bind=self.engine,
            class_=AsyncSession,
            autoflush=False,
            autocommit=False,
            expire_on_commit=False,
        )

    def get_scopes_session(self):
        session = async_scoped_session(
            session_factory=self.session_factory,
            scopefunc=current_task,
        )
        return session

    async def session_dependency(self) -> AsyncSession:
        async with self.session_factory() as session:
            yield session
            await session.close()

    async def scoped_session_dependency(self) -> AsyncSession:
        session = self.get_scopes_session()
        yield session
        await session.close()


db_helper = DataBaseHelper(
    url=settings.DB_URL,
    echo=settings.DB_ECHO
)
