from sqlalchemy import select, insert

from app.repository.base import BaseDAO
from app.database import async_session_maker

from app.users.models import Roles


class RoleDAO(BaseDAO):
    model = Roles

    @classmethod
    async def add(cls, name: str):
        async with async_session_maker() as session:
            new_role = (
                insert(Roles)
                .values(
                    name=name
                )
                .returning(Roles)
            )
            add_new_role = await session.execute(new_role)
            await session.commit()
            return add_new_role.scalars()

    @staticmethod
    async def find_one_by_name(name: str):
        async with async_session_maker() as session:
            result = await session.execute(select(Roles).where(Roles.name == name))
            return result.scalar_one_or_none()