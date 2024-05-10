from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.users.router import router as users_router
from app.roles.router import router as roles_router
from app.tasks.router import router as tasks_router

app = FastAPI(
    title='CRM_system'
)

origins = [
    "localhost",
    "localhost:9000",
    "http://localhost:5173",
    "http://localhost:5174",
    "http://localhost:5175",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTION", "DELETE", "PATCH", "PUT"],
    allow_headers=["Content-type", "Set-Cookie", "Access-Control-Allow-Headers", "Access-Authorization"]
)

app.include_router(users_router)
app.include_router(roles_router)
app.include_router(tasks_router)

