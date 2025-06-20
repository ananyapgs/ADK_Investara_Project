from adk.web import app  # Use the actual import used by ADK for its FastAPI app
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import os

# Get root directory
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# Mount static folders
app.mount("/css_styles", StaticFiles(directory=os.path.join(ROOT_DIR, "css_styles")), name="css")
app.mount("/images", StaticFiles(directory=os.path.join(ROOT_DIR, "images")), name="images")

# Override "/" to serve your custom index.html
@app.get("/", include_in_schema=False)
def serve_index():
    return FileResponse(os.path.join(ROOT_DIR, "index.html"))
