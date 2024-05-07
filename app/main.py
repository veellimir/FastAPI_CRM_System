from fastapi import FastAPI

app = FastAPI(
    title='CRM_system'
)


@app.get('/новый проект')
def hello():
    return 'start project'
