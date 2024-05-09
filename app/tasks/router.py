from fastapi import APIRouter, Depends

from app.tasks.dao import TaskDAO
from app.users.dependecies import current_user
from app.users.models import Users
from app.exeptions import TokenAbsentException

from datetime import date

router = APIRouter(
    prefix="/tasks",
    tags=["Задачи"]
)


@router.post("/add/task")
async def add_task(
        name_task: str,
        date_create: date,
        deadline: date,
        description: str = None,
        user_id: int = None,
):
    task = await TaskDAO.add(user_id, name_task, description, date_create, deadline)
    return task


@router.get(
    "/all_task",
    summary="получить список всех задач"
)
async def get_all_tasks(users: Users = Depends(current_user)):
    return await TaskDAO.find_all()


@router.get(
    "/get_task/user",
    summary="получить список задач текущего пользователя"
)
async def get_task_current_user(user: Users = Depends(current_user)):
    if not user:
        raise TokenAbsentException
    return await TaskDAO.find_all(user_id=user.id)