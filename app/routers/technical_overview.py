from fastapi import APIRouter, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from jinja2 import TemplateNotFound

router = APIRouter(prefix="/technical_overview")
templates = Jinja2Templates(directory="templates/technical_overview/")


@router.get("/", response_class=HTMLResponse)
async def general_overview(request: Request):
    return templates.TemplateResponse("technical_overview.html", {"request": request})
