from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import uvicorn
from routers import home, general_overview, technical_overview
import os


app = FastAPI()

# Include routers
app.include_router(home.router)
app.include_router(general_overview.router)
app.include_router(technical_overview.router)

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")
app.mount("/images", StaticFiles(directory="static/images"), name="images")
app.mount("/videos", StaticFiles(directory="static/videos"), name="videos")


def main():
    """Run the FastAPI application."""
    host = os.getenv("HOST", "0.0.0.0")
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host=host, port=port)


if __name__ == "__main__":
    main()
