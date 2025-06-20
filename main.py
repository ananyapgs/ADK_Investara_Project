from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# ✅ Make sure directories exist
css_dir = os.path.join(BASE_DIR, "css_styles")
img_dir = os.path.join(BASE_DIR, "images")

if not os.path.exists(css_dir):
    raise RuntimeError(f"Missing directory: {css_dir}")
if not os.path.exists(img_dir):
    raise RuntimeError(f"Missing directory: {img_dir}")

# Mount static files
app.mount("/css_styles", StaticFiles(directory=css_dir), name="css")
app.mount("/images", StaticFiles(directory=img_dir), name="images")

@app.get("/", include_in_schema=False)
def serve_index():
    return FileResponse(os.path.join(BASE_DIR, "index.html"))

@app.get("/navigation.html", include_in_schema=False)
def serve_nav():
    return FileResponse(os.path.join(BASE_DIR, "navigation.html"))

@app.get("/visualization.html", include_in_schema=False)
def serve_vis():
    return FileResponse(os.path.join(BASE_DIR, "visualization.html"))

@app.get("/finance-guide.html", include_in_schema=False)
def serve_guide():
    return FileResponse(os.path.join(BASE_DIR, "finance-guide.html"))
