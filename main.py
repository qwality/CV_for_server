from fastapi import FastAPI, Request, Response, status
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()

templates = Jinja2Templates(directory='templates')

app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static")
app.mount(
    "/.well-known",
    StaticFiles(directory='static/.well-known'),
    name='cert')

@app.get('/')
async def index(request: Request):
    return templates.TemplateResponse('main_cv.html', {'request':request})

@app.head('/')
async def head(request: Request):
    return None

@app.get('/test')
async def test_end_point(request: Request):
    return 'test resonse from uvicorn'

@app.get('/request-headers')
async def request_headers(request: Request):
    return dict(request.headers)

@app.get('/{path:path}')
async def catch_other(request: Request, path: str):
    return f"Toto je catch-all koncový bod pro cestu: {path}"


@app.get('/studiaLB')
async def redirect_to_8080(request: Request):
    return Response(
        status_code=status.HTTP_307_TEMPORARY_REDIRECT,
        headers={
            'Location': 'http://localhost:8080'
        }
    )