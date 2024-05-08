from repository.base import BaseDAO
from database import async_session_maker

from tasks.models import Tasks

from datetime import date

from sqlalchemy import insert


class TaskDAO(BaseDAO):
    model = Tasks

    @classmethod
    async def add(
            cls,
            name_task: str,
            description: str,
            date_create: date,
            deadline: date,
    ):
        async with async_session_maker() as session:
            new_task = (
                insert(Tasks)
                .values(
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
