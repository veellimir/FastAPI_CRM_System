from datetime import date

from fastapi import APIRouter, Depends

from app.projects.dao import ProjectDAO, ProjectUserDAO

from app.users.dependecies import current_user
from app.users.models import Users

router = APIRouter(
    prefix="/project",
    tags=["Проекты"]
)


@router.post(
    "/create",
    summary="создать проект"
)
async def create_project(name: str, description: str, date_create: date):
    project_data = {
        "name": name,
        "description": description,
        "date_create": date_create
    }
    project = await ProjectDAO.add_project(**project_data)
    return f"Проект: {name} создан"


@router.get(
    "/all",
    summary="получить список всех проектов"
)
async def all_projects(users: Users = Depends(current_user)):
    projects = await ProjectDAO.find_all()
    return projects


@router.get(
    "/{user_id}",
    summary="получить проекты пользователя"
)
async def get_project_id(user_id: int, users: Users = Depends(current_user)):
    projects = await ProjectUserDAO.find_projects_by_user_id(user_id)
    return projects



