from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from google.adk.app import create_app
import os

# ✅ Create app using Google ADK (loads your agents like nifty_agent)
adk_app = create_app()

# ✅ Create a wrapper FastAPI app
app = FastAPI()

# ✅ Mount ADK app at /adk
app.mount("/adk", adk_app)

# ✅ Serve frontend files (adjust path if your HTML is one level up)
frontend_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

app.mount("/static", StaticFiles(directory=frontend_dir), name="static")

# ✅ Optional: serve index.html directly at root
@app.get("/")
def root():
    return FileResponse(os.path.join(frontend_dir, "index.html"))
