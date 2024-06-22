from fastapi import APIRouter, Request, Depends
from fastapi.responses import HTMLResponse
from jinja2 import Environment, FileSystemLoader
from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId
import os

router = APIRouter()

# Set up Jinja2 environment
templates = Environment(loader=FileSystemLoader('templates'))

# MongoDB connection (using environment variable for MongoDB URL)
mongo_url = os.getenv("MONGO_URL", "mongodb://admin:admin@mongodb:27017")
client = AsyncIOMotorClient(mongo_url)
db = client['admin']
collection = db['content']

async def get_content(title: str):
    content = await collection.find_one({"title": title})
    return content

@router.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    content = await get_content("Semiconductor Processing Overview")
    print("content", content)
    template = templates.get_template('index.html')
    return template.render(request=request, content=content)


@router.get("/course_overview", response_class=HTMLResponse)
async def read_course_overview(request: Request):
    content = await get_content("Course Overview")
    template = templates.get_template('course_overview.html')
    return template.render(request=request, content=content)

@router.get("/general_overview", response_class=HTMLResponse)
async def read_course_overview(request: Request):
    content = await get_content("General Overview")
    template = templates.get_template('general_overview.html')
    return template.render(request=request, content=content)

# @router.get("/general_overview/{chapter}", response_class=HTMLResponse)
# async def read_general_overview_chapter(request: Request, chapter: str):
#     content = await get_content("General Overview")
#     chapter_content = next((ch for ch in content['chapters'] if ch['url'].endswith(chapter)), {})
#     template = templates.get_template('general_overview.html')
#     return template.render(request=request, content=chapter_content)


@router.get("/technical_overview", response_class=HTMLResponse)
async def read_technical_overview(request: Request):
    content = await get_content("your_technical_overview_page_id_here")
    template = templates.get_template('technical_overview.html')
    return template.render(request=request, content=content)

@router.get("/general_overview/introduction", response_class=HTMLResponse)
async def read_introduction(request: Request):
    content = await get_content("Introduction")
    template = templates.get_template('introduction.html')
    return template.render(request=request, content=content)

@router.get("/general_overview/introduction/objectives", response_class=HTMLResponse)
async def read_objectives(request: Request):
    content = await get_content("Objectives")
    template = templates.get_template('objectives.html')
    return template.render(request=request, content=content)
