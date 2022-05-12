from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates

view = APIRouter()

templates = Jinja2Templates(directory="templates")


@view.get("/", response_class=JSONResponse)
async def home() -> JSONResponse:
    """Home Page

    Returns:
        JSONResponse: Hello World!
    """
    message = {"stauts": "success", "message": "Hello World!"}
    return JSONResponse(content=message)

@view.get("/home", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
