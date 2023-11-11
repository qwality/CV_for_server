from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()

templates = Jinja2Templates(directory='templates')

app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static")
app.mount(
    "/.well-known/acme-challenge",
    StaticFiles(directory='static/.well-known/acme-challenge'),
    name='cert')

@app.get('/')
async def index(request: Request):
    return templates.TemplateResponse('main_cv.html', {'request':request})

# @app.