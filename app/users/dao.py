from sqlalchemy import select

from app.users.models import Users

from app.repository.base import BaseDAO
from app.database import async_session_maker


class UsersDAO(BaseDAO):
    model = Users

    @classmethod
    async def find_one_or_none_users(cls, email: str):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(email=email)
            result = await session.execute(query)
            return result.scalar_one_or_none()
