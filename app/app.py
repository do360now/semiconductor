from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import uvicorn
from routers import pages

app = FastAPI()

# Include routers
app.include_router(pages.router)

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")
app.mount("/images", StaticFiles(directory="images"), name="images")
app.mount("/videos", StaticFiles(directory="videos"), name="videos")

def main():
    uvicorn.run(app, host="127.0.0.1", port=8080)

if __name__ == "__main__":
    main()
