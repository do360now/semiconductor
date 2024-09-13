from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

# Import the version from the __version__.py file
from __version__ import __version__

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "version": __version__})

@router.get("/about_spo", response_class=HTMLResponse)
async def about_spo(request: Request):
    return templates.TemplateResponse("about_spo.html", {"request": request})

@router.get("/glossary", response_class=HTMLResponse)
async def glossary(request: Request):
    return templates.TemplateResponse("glossary.html", {"request": request})

@router.get("/course_overview", response_class=HTMLResponse)
async def course_overview(request: Request):
    return templates.TemplateResponse("course_overview.html", {"request": request})
