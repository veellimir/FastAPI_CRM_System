from fastapi import FastAPI

from app.users.router import router as user_router
from app.tasks.router import router as task_router

app = FastAPI(
    title='CRM_system'
)


app.include_router(user_router)
app.include_router(task_router)

