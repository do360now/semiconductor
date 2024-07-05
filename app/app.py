from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import uvicorn
from routers import pages

app = FastAPI()
app.include_router(pages.router)

def main():
    mount()

    uvicorn.run(app, host="0.0.0.0", port=8000)

def mount():
    # Include routers
    
    # Mount static files
    app.mount("/static", StaticFiles(directory="static"), name="static")
    app.mount("/images", StaticFiles(directory="images"), name="images")
    app.mount("/videos", StaticFiles(directory="videos"), name="videos")


if __name__ == "__main__":
    main()
