from fastapi import APIRouter, Depends

from tasks.dao import TaskDAO
from users.dependecies import current_user
from users.models import Users
from exeptions import TokenAbsentException

from datetime import date

router = APIRouter(
    prefix="/tasks",
    tags=["Задачи"]
)


@router.post("/add/task")
async def add_task(
        name_task: str,
        description: str,
        date_create: date,
        deadline: date,
):
    task = await TaskDAO.add(name_task, description, date_create, deadline)
    return task


@router.get(
    "/all_task",
    summary="получить список всех задач"
)
async def get_all_tasks(users: Users = Depends(current_user)):
    return await TaskDAO.find_all()


@router.get(
    "/get_task/user/{user_id}",
    summary="получить список задач пользователя"
)
async def get_task_current_user(user_id: int, Users = Depends(current_user)):
    if not user_id:
        raise TokenAbsentException
    return await TaskDAO.find_by_id(user_id)
