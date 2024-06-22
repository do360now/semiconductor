import logging
import fastapi
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles



router = APIRouter()
templates = Jinja2Templates(directory="templates")
logger = logging.getLogger(__name__)


@router.get("/tutorial", response_class=HTMLResponse)
async def read_tutorial(request: Request):
    content = await get_content("your_tutorial_page_id_here")
    template = templates.get_template('tutorial.html')
    return template.render(request=request, content=content)
