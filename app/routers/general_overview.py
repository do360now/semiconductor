from fastapi import APIRouter, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from jinja2 import TemplateNotFound

router = APIRouter(prefix="/general_overview")
templates = Jinja2Templates(directory="app/templates/general_overview/")


@router.get("/", response_class=HTMLResponse)
async def general_overview(request: Request):
    return templates.TemplateResponse("general_overview.html", {"request": request})


@router.get("/introduction", response_class=HTMLResponse)
async def introduction(request: Request):
    return templates.TemplateResponse("introduction.html", {"request": request})


@router.get("/introduction/{page_name}", response_class=HTMLResponse)
async def read_page(request: Request, page_name: str):
    template_name = f"introduction/{page_name}.html"
    try:
        return templates.TemplateResponse(template_name, {"request": request})
    except TemplateNotFound:
        raise HTTPException(status_code=404, detail="Page not found")
