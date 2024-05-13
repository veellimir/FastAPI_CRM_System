from app.users.models import Users

from app.repository.base import BaseDAO
from app.database import async_session_maker


class UsersDAO(BaseDAO):
    model = Users

    @classmethod
    async def upload_user_image(cls, user_id: int, filename: str):
        async with async_session_maker() as session:
            async with session.begin():
                user = await session.get(cls.model, user_id)
                if not user:
                    return None
                else:
                    user.user_image = filename
                    await session.commit()
                    return user
