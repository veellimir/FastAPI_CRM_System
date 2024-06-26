from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.users.router import router as auth_router
from app.users_data.router import router as users_router
from app.roles.router import router as roles_router
from app.projects.router import router as projects_router
from app.tasks.router import router as tasks_router
from app.finance.router import router as finance_router

app = FastAPI(
    title='CRM_system'
)

origins = [
    # "localhost:9000",
    "https://crm-sistem-daniilkuns-projects.vercel.app",
    "https://crm-sistem-daniilkuns-projects.vercel.app/auth/login",
    "http://localhost:5173",
    "http://localhost:5174",
    "http://localhost:5175",
    "http://127.0.0.1:5500"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"],
    allow_headers=["Content-type", "Set-Cookie", "Access-Control-Allow-Headers", "Authorization"]
)

app.include_router(auth_router)
app.include_router(users_router)
app.include_router(roles_router)
app.include_router(projects_router)
app.include_router(tasks_router)
app.include_router(finance_router)

