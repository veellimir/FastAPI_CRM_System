from datetime import date

from fastapi import APIRouter, Depends

from app.tasks.dao import TaskDAO
from app.users.dependecies import current_user
from app.users.models import Users

from app.exceptions import TokenAbsentException

router = APIRouter(
    prefix="/tasks",
    tags=["Задачи"]
)


@router.post(
    "/create/{name_task}/{date_create}/{deadline}",
    summary="создать задачу",

)
async def add_task(
        name_task: str,
        date_create: date,
        deadline: date,
        description: str = None,
        user_id: int = None,
        users: Users = Depends(current_user)
):
    task_data = {
        "name_task": name_task,
        "description": description,
        "date_create": date_create,
        "deadline": deadline,
        "user_id": user_id
    }
    task = await TaskDAO.add_kwargs(**task_data)
    return f"Задача: {name_task} создана"


@router.patch(
    "/edit/{task_id}",
    summary="редактировать задачу"
)
async def edit_task(
        task_id: int,
        name_task: str = None,
        deadline: date = None,
        description: str = None,
        user_id: int = None,
        users: Users = Depends(current_user)
):
    task = await TaskDAO.update_task(task_id, name_task, deadline, description, user_id)
    return f"Задача: {name_task} отредактирована"


@router.delete(
    "/delete/{task_id}",
    summary="удалить задачу"
)
async def delete_task(task_id: int, users: Users = Depends(current_user)):
    task = await TaskDAO.delete(task_id)
    return f"Задача удалена"


@router.get(
    "/all",
    summary="получить список всех задач"
)
async def get_all_tasks(users: Users = Depends(current_user)):
    return await TaskDAO.find_all()


@router.get(
    "/current_user",
    summary="получить список задач текущего пользователя"
)
async def get_task_current_user(user: Users = Depends(current_user)):
    if not user:
        raise TokenAbsentException
    return await TaskDAO.find_all(user_id=user.id)


@router.get(
    "/project{project_id}",
    summary="получить список задач по проекту"
)
async def get_task_project(project_id: int, users: Users = Depends(current_user)):
    project = await TaskDAO.find_by_id(project_id)
    return project
