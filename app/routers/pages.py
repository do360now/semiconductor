from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from jinja2 import Environment, FileSystemLoader
import os
import markdown

router = APIRouter()

# Set up Jinja2 environment
templates = Environment(loader=FileSystemLoader('templates'))

# Helper function to render templates
def render_template(template_name: str, request: Request):
    template = templates.get_template(template_name)
    return template.render(request=request)

# Path to the .md file
MD_FILE_PATH = "tech_overview.md"


# Currently, the markdown content is read from a file and converted to HTML.  Not a lot of styling is applied to the HTML content.
@router.get("/technical_overview", response_class=HTMLResponse)
async def read_md_as_html():
    with open(MD_FILE_PATH, "r") as md_file:
        content = md_file.read()
        # Convert markdown content to HTML
        html_content = markdown.markdown(content)
        return HTMLResponse(content=html_content)

@router.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return render_template('index.html', request)

@router.get("/about_spo", response_class=HTMLResponse)
async def read_root(request: Request):
    return render_template('about_spo.html', request)

@router.get("/glossary", response_class=HTMLResponse)
async def read_root(request: Request):
    return render_template('glossary.html', request)

@router.get("/course_overview", response_class=HTMLResponse)
async def read_course_overview(request: Request):
    return render_template('course_overview.html', request)

@router.get("/general_overview", response_class=HTMLResponse)
async def read_general_overview(request: Request):
    return render_template('general_overview.html', request)

@router.get("/technical_overview", response_class=HTMLResponse)
async def read_technical_overview(request: Request):
    return render_template('technical_overview.html', request)

@router.get("/general_overview/introduction", response_class=HTMLResponse)
async def read_introduction(request: Request):
    return render_template('introduction.html', request)

@router.get("/general_overview/introduction/objectives", response_class=HTMLResponse)
async def read_objectives(request: Request):
    return render_template('objectives.html', request)

@router.get("/general_overview/introduction/electricity_electronics", response_class=HTMLResponse)
async def read_electricity_electronics(request: Request):
    return render_template('electricity_electronics.html', request)

@router.get("/general_overview/introduction/history_electronics", response_class=HTMLResponse)
async def read_history_electronics(request: Request):
    return render_template('history_electronics.html', request)

@router.get("/general_overview/introduction/vacuum_tubes", response_class=HTMLResponse)
async def read_vacuum_tubes(request: Request):
    return render_template('vacuum_tubes.html', request)

@router.get("/general_overview/introduction/solid_state", response_class=HTMLResponse)
async def read_solid_state(request: Request):
    return render_template('solid_state.html', request)

@router.get("/general_overview/introduction/integrated_circuits", response_class=HTMLResponse)
async def read_integrated_circuits(request: Request):
    return render_template('integrated_circuits.html', request)

@router.get("/general_overview/introduction/analog_and_digital", response_class=HTMLResponse)
async def read_analog_and_digital(request: Request):
    return render_template('analog_and_digital.html', request)

@router.get("/general_overview/introduction/amplitude", response_class=HTMLResponse)
async def read_analog_and_digital(request: Request):
    return render_template('amplitude.html', request)

@router.get("/general_overview/introduction/frequency", response_class=HTMLResponse)
async def read_analog_and_digital(request: Request):
    return render_template('frequency.html', request)

@router.get("/general_overview/introduction/binary_counting", response_class=HTMLResponse)
async def read_binary_counting(request: Request):
    return render_template('binary_counting.html', request)

@router.get("/general_overview/introduction/digital_logic", response_class=HTMLResponse)
async def read_digital_logic(request: Request):
    return render_template('digital_logic.html', request)

@router.get("/general_overview/introduction/integrated_circuit_development", response_class=HTMLResponse)
async def read_integrated_circuit_development(request: Request):
    return render_template('integrated_circuit_development.html', request)

@router.get("/general_overview/introduction/integrated_circuit_development2", response_class=HTMLResponse)
async def read_integrated_circuit_development2(request: Request):
    return render_template('integrated_circuit_development2.html', request)

@router.get("/general_overview/introduction/small_scale_devices", response_class=HTMLResponse)
async def read_small_scale_devices(request: Request):
    return render_template('small_scale_devices.html', request)

@router.get("/general_overview/introduction/medium_scale_devices", response_class=HTMLResponse)
async def read_medium_scale_devices(request: Request):
    return render_template('medium_scale_devices.html', request)

@router.get("/general_overview/introduction/large_scale_devices", response_class=HTMLResponse)
async def read_large_scale_devices(request: Request):
    return render_template('large_scale_devices.html', request)

@router.get("/general_overview/introduction/very_large_scale_devices", response_class=HTMLResponse)
async def read_very_large_scale_devices(request: Request):
    return render_template('very_large_scale_devices.html', request)

@router.get("/general_overview/introduction/ultra_large_scale_devices", response_class=HTMLResponse)
async def read_ultra_large_scale_devices(request: Request):
    return render_template('ultra_large_scale_devices.html', request)

