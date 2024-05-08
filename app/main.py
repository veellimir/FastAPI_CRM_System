from fastapi import FastAPI

from users.router import router as user_router

app = FastAPI(
    title='CRM_system'
)


app.include_router(user_router)

