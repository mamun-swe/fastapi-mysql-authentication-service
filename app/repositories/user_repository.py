from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.user import User
from app.schemas.user import CreateUserSchema, UpdateUserSchema


class UserRepository:

    # Get all users
    async def get_users(self, db: AsyncSession):
        results = await db.execute(select(User))
        return results.scalars().all()
