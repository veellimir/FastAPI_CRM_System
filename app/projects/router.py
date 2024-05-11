from fastapi import APIRouter, Depends

from app.projects.dao import ProjectDAO, ProjectUserDAO

from app.users.dependecies import current_user
from app.users.models import Users

router = APIRouter(
    prefix="/project",
    tags=["Проекты"]
)


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
async def get_project_id(user_id: int):
    projects = await ProjectUserDAO.find_projects_by_user_id(user_id)
    return projects



