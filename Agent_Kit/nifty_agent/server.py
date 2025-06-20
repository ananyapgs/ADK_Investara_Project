from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from google.adk import Agent
from pathlib import Path

app = FastAPI()

# ✅ Base directory (Agent_Kit/)
BASE_DIR = Path(__file__).resolve().parent.parent

# Static file mounts
app.mount("/css_style", StaticFiles(directory=BASE_DIR / "css_styles"), name="css")
app.mount("/images", StaticFiles(directory=BASE_DIR / "images"), name="images")

# Serve static pages
@app.get("/")
def read_root():
    return FileResponse(BASE_DIR / "index.html")

@app.get("/navigation")
def navigation():
    return FileResponse(BASE_DIR / "navigation.html")

@app.get("/visualization")
def visualization():
    return FileResponse(BASE_DIR / "visualization.html")

# Register agent
from nifty_agent.agent import root_agent
root_agent.mount_to_app(app)
