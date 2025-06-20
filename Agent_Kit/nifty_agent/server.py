from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from google.adk import Agent
from pathlib import Path
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

# Create FastAPI app
app = FastAPI()

# Base directory to locate static files
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Static file mounts
css_path = BASE_DIR / "css_styles"
img_path = BASE_DIR / "images"
kit_path = BASE_DIR / "Agent_Kit"

# Check if directories exist before mounting
if css_path.exists():
    app.mount("/css_style", StaticFiles(directory=css_path), name="css")
else:
    print(f"[WARNING] Static mount failed: {css_path} does not exist")

if img_path.exists():
    app.mount("/images", StaticFiles(directory=img_path), name="images")
else:
    print(f"[WARNING] Static mount failed: {img_path} does not exist")

if kit_path.exists():
    app.mount("/Agent_Kit", StaticFiles(directory=kit_path), name="agent_kit")
else:
    print(f"[WARNING] Static mount failed: {kit_path} does not exist")

# Serve static HTML pages
@app.get("/")
def read_root():
    return FileResponse(BASE_DIR / "index.html")

@app.get("/navigation")
def navigation():
    return FileResponse(BASE_DIR / "navigation.html")

@app.get("/visualization")
def visualization():
    return FileResponse(BASE_DIR / "visualization.html")

# Register the ADK agent
from nifty_agent.agent import root_agent
root_agent.mount_to_app(app)
