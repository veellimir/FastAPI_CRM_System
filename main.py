from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.users.router import router as user_router
from app.tasks.router import router as task_router

app = FastAPI(
    title='CRM_system'
)

origins = [
    '*'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTION", "DELETE", "PATCH", "PUT"],
    allow_headers=["Content-type", "Set-Cookie", "Access-Control-Allow-Headers", "Access-Authorization"]
)

app.include_router(user_router)
app.include_router(task_router)

