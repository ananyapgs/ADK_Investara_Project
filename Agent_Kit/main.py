from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import os

# Initialize the FastAPI app
app = FastAPI()

# Serve static assets
app.mount("/css_styles", StaticFiles(directory="../css_styles"), name="css")
app.mount("/images", StaticFiles(directory="../images"), name="images")

# Serve index.html from root
@app.get("/")
def serve_index():
    return FileResponse("../index.html")
