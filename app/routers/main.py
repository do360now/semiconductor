from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from __version__ import __version__  # Import the version from __version__.py

import os

router = APIRouter()
templates = Jinja2Templates(directory="templates")

# Initialize visitor count variable
visitor_count_file = "/app/visitor_data/visitor_count.txt"

# def get_visitor_count():
#     if os.path.exists(visitor_count_file):
#         with open(visitor_count_file, 'r') as f:
#             return int(f.read())
    # return 0

# def increment_visitor_count():
#     count = get_visitor_count() + 1
#     with open(visitor_count_file, 'w') as f:
#         f.write(str(count))
#     return count

def increment_visitor_count():
    try:
        # Try to open the file and read the current count
        with open(visitor_count_file, "r") as f:
            count = int(f.read())
    except FileNotFoundError:
        # If the file doesn't exist, initialize the count to 0
        count = 0
    # Incrememt the visitor count
    count += 1

    # Write the new count back to the file
    with open(visitor_count_file, "w") as f:
        f.write(str(count))
    return count


# Main index route
@router.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "version": __version__})

# Visitor count route
@router.get("/visitor-count", response_class=JSONResponse)
async def visitor_count():
    count = increment_visitor_count()
    return {"count": count}

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
