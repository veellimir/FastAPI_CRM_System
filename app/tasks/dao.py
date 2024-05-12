from datetime import date

from sqlalchemy import insert, update

from app.repository.base import BaseDAO
from app.database import async_session_maker

from app.tasks.models import Tasks


class TaskDAO(BaseDAO):
    model = Tasks

    # @classmethod
    # async def add(
    #         cls,
    #         name_task: str,
    #         description: str,
    #         date_create: date,
    #         deadline: date,
    #         user_id: int = None,
    # ):
    #     async with async_session_maker() as session:
    #         new_task = (
    #             insert(Tasks)
    #             .values(
    #                 name_task=name_task,
    #                 description=description,
    #                 date_create=date_create,
    #                 deadline=deadline,
    #                 user_id=user_id,
    #             )
    #             .returning(Tasks)
    #         )
    #         add_new_task = await session.execute(new_task)
    #         await session.commit()
    #         return add_new_task.scalars()

    @classmethod
    async def update_task(
            cls,
            task_id: int,
            name_task: str,
            deadline: date = None,
            description: str = None,
            user_id: int = None
    ):
        async with async_session_maker() as session:
            task = (
                update(Tasks)
                .where(Tasks.id == task_id)
                .values(
                    name_task=name_task or Tasks.name_task,
                    deadline=deadline or Tasks.deadline,
                    description=description or Tasks.description,
                    user_id=user_id or Tasks.user_id
                )
                .returning(Tasks)
            )
            update_task = await session.execute(task)
            await session.commit()
            return update_task.scalars()
