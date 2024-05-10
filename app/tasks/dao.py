from datetime import date

from sqlalchemy import insert

from app.repository.base import BaseDAO
from app.database import async_session_maker

from app.tasks.models import Tasks


class TaskDAO(BaseDAO):
    model = Tasks

    @classmethod
    async def add(
            cls,
            user_id: int,
            name_task: str,
            description: str,
            date_create: date,
            deadline: date,
    ):
        async with async_session_maker() as session:
            new_task = (
                insert(Tasks)
                .values(
                    user_id=user_id,
                    name_task=name_task,
                    description=description,
                    date_create=date_create,
                    deadline=deadline,
                )
                .returning(Tasks)
            )
            add_new_task = await session.execute(new_task)
            await session.commit()
            return add_new_task.scalars()
