from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import uvicorn
from .routers import home, general_overview, technical_overview


app = FastAPI()

# Include routers
app.include_router(home.router)
app.include_router(general_overview.router)
app.include_router(technical_overview.router)


# Mount static files
app.mount("/static", StaticFiles(directory="app/static"), name="static")
app.mount("/images", StaticFiles(directory="app/static/images"), name="images")
app.mount("/videos", StaticFiles(directory="app/static/videos"), name="videos")


def main():
    uvicorn.run(app, host="0.0.0.0", port=80)


if __name__ == "__main__":
    main()
