from fastapi import FastAPI, Request, Response, status
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()
'''FastAPI app reference'''

templates = Jinja2Templates(directory='templates')
''' specifies usage of jinja2 templating engine and defines its root directory
    templates'''

app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static")
'''making entire /static directory and all its subdirectories publicaly awiable'''

app.mount(
    "/.well-known",
    StaticFiles(directory='static/.well-known'),
    name='cert')
'''for SSL'''

@app.get('/')
async def index(request: Request):
    return templates.TemplateResponse('main_cv.html', {'request':request})

@app.head('/')
async def head(request: Request):
    '''only here to allow HTTP head request'''
    return None

@app.get('/test')
async def test_end_point(request: Request):
    '''specific test endpoint'''
    return '<test resonse from uvicorn>'

@app.get('/request-headers')
async def request_headers(request: Request):
    '''test headers by returning all headers sent in request'''
    return dict(request.headers)

@app.get('/{path:path}')
async def catch_other(request: Request, path: str):
    '''replaces 404'''
    return f"Toto je catch-all koncový bod pro cestu: <{path}>\n tento endpoint nahrazuje 404"


# @app.get('/studiaLB')
# async def redirect_to_8080(request: Request):
#     return Response(
#         status_code=status.HTTP_307_TEMPORARY_REDIRECT,
#         headers={
#             'Location': 'http://localhost:8080'
#         }
#     )