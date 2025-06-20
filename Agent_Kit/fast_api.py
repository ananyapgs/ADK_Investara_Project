from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from google.adk.app import create_app
import os

# ✅ Create ADK app
adk_app = create_app()

# ✅ Create main FastAPI app
app = FastAPI()

# ✅ Mount ADK app at /adk
app.mount("/adk", adk_app)

# ✅ Set up base directory
frontend_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# ✅ Serve static folders
app.mount("/css_styles", StaticFiles(directory=os.path.join(frontend_dir, "css_styles")), name="css")
app.mount("/images", StaticFiles(directory=os.path.join(frontend_dir, "images")), name="images")

# ✅ Serve HTML pages
@app.get("/")
def root():
    return FileResponse(os.path.join(frontend_dir, "index.html"))

@app.get("/navigation")
def navigation():
    return FileResponse(os.path.join(frontend_dir, "navigation.html"))

@app.get("/visualization")
def visualization():
    return FileResponse(os.path.join(frontend_dir, "visualization.html"))
