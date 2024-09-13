from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import uvicorn
from app.routers import main, general_overview, technical_overview

app = FastAPI()

# Include routers
app.include_router(main.router)
app.include_router(general_overview.router)

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")
app.mount("/images", StaticFiles(directory="images"), name="images")
app.mount("/videos", StaticFiles(directory="videos"), name="videos")

def main():
    uvicorn.run(app, host="0.0.0.0", port=80)

if __name__ == "__main__":
    main()
