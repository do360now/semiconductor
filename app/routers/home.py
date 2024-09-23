from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from __version__ import (
    __version__,
)  # Adjust the import to point to the correct module
from routers import home, general_overview, technical_overview

import os

router = APIRouter()
templates = Jinja2Templates(directory="templates")


# Main index route
@router.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "version": __version__})


# Other routes
@router.get("/about_spo", response_class=HTMLResponse)
async def about_spo(request: Request):
    return templates.TemplateResponse("about_spo.html", {"request": request})


@router.get("/glossary", response_class=HTMLResponse)
async def glossary(request: Request):
    return templates.TemplateResponse("glossary.html", {"request": request})


@router.get("/course_overview", response_class=HTMLResponse)
async def course_overview(request: Request):
    return templates.TemplateResponse("course_overview.html", {"request": request})
