from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Remove the checks if they block deploy
app.mount("/css_styles", StaticFiles(directory=os.path.join(BASE_DIR, "css_styles")), name="css")
app.mount("/images", StaticFiles(directory=os.path.join(BASE_DIR, "images")), name="images")

@app.get("/", include_in_schema=False)
def serve_index():
    return FileResponse(os.path.join(BASE_DIR, "index.html"))

@app.get("/visualization.html", include_in_schema=False)
def serve_vis():
    return FileResponse(os.path.join(BASE_DIR, "visualization.html"))

@app.get("/navigation.html", include_in_schema=False)
def serve_nav():
    return FileResponse(os.path.join(BASE_DIR, "navigation.html"))

@app.get("/finance-guide.html", include_in_schema=False)
def serve_guide():
    return FileResponse(os.path.join(BASE_DIR, "finance-guide.html"))
