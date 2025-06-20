from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI()

# Serve static folders
app.mount("/css_styles", StaticFiles(directory="css_styles"), name="css")
app.mount("/images", StaticFiles(directory="images"), name="images")

# Serve HTML files
@app.get("/")
def get_index():
    return FileResponse("index.html")

@app.get("/navigation")
def get_navigation():
    return FileResponse("navigation.html")

@app.get("/visualization")
def get_visualization():
    return FileResponse("visualization.html")

@app.get("/finance-guide")
def get_guide():
    return FileResponse("finance-guide.html")
