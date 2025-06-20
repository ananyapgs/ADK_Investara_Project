from adk.web import app  # Adjust if ADK exposes app differently
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import os

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# Mount static files
app.mount("/css_styles", StaticFiles(directory=os.path.join(ROOT_DIR, "css_styles")), name="css")
app.mount("/images", StaticFiles(directory=os.path.join(ROOT_DIR, "images")), name="images")

# Serve frontend pages
@app.get("/")
def serve_index():
    return FileResponse(os.path.join(ROOT_DIR, "index.html"))

@app.get("/navigation")
def serve_navigation():
    return FileResponse(os.path.join(ROOT_DIR, "navigation.html"))

@app.get("/finance-guide")
def serve_guide():
    return FileResponse(os.path.join(ROOT_DIR, "finance-guide.html"))

@app.get("/visualization")
def serve_visualization():
    return FileResponse(os.path.join(ROOT_DIR, "visualization.html"))
