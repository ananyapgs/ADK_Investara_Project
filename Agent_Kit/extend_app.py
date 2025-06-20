from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI()

# Root directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Serve static files
app.mount("/css_styles", StaticFiles(directory=os.path.join(BASE_DIR, "css_styles")), name="css")
app.mount("/images", StaticFiles(directory=os.path.join(BASE_DIR, "images")), name="images")

# Serve HTML files
@app.get("/")
def get_index():
    return FileResponse(os.path.join(BASE_DIR, "index.html"))

@app.get("/navigation.html")
def get_navigation():
    return FileResponse(os.path.join(BASE_DIR, "navigation.html"))

@app.get("/visualization.html")
def get_visualization():
    return FileResponse(os.path.join(BASE_DIR, "visualization.html"))

@app.get("/finance-guide.html")
def get_guide():
    return FileResponse(os.path.join(BASE_DIR, "finance-guide.html"))
