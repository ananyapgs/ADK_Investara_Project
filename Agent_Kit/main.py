from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI()

# Absolute project root (one level above Agent_Kit)
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# Serve static files
app.mount("/css_styles", StaticFiles(directory=os.path.join(PROJECT_ROOT, "css_styles")), name="css")
app.mount("/images", StaticFiles(directory=os.path.join(PROJECT_ROOT, "images")), name="images")

# Serve index.html
@app.get("/")
def serve_index():
    return FileResponse(os.path.join(PROJECT_ROOT, "index.html"))
