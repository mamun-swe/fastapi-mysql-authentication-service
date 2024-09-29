from databases import Database
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "mysql+aiomysql://root:root%40root@localhost/fastapi-auth"

database = Database(DATABASE_URL)

# Set up the async SQLAlchemy engine and session
engine = create_async_engine(DATABASE_URL, echo=True, future=True)
async_session = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)


# Dependency to get the async session for the request
async def get_db():
    async with async_session() as session:
        yield session
