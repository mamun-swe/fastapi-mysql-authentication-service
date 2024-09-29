from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.user_repository import UserRepository


class UserService:
    def __init__(self):
        self.user_repository = UserRepository()

    async def get_all_users(self, db: AsyncSession):
        return await self.user_repository.get_users(db)
