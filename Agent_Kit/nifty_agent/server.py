from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from google.adk import Agent

app = FastAPI()

# ✅ Mount static files
app.mount("/css_style", StaticFiles(directory="css_style"), name="css")
app.mount("/images", StaticFiles(directory="images"), name="images")
app.mount("/Agent_Kit", StaticFiles(directory="Agent_Kit"), name="agent_kit")

# ✅ Serve index.html on "/"
@app.get("/")
def read_root():
    return FileResponse("index.html")

# ✅ Add other pages if needed
@app.get("/navigation")
def navigation():
    return FileResponse("navigation.html")

@app.get("/visualization")
def visualization():
    return FileResponse("visualization.html")

# ✅ Register your ADK agent
from nifty_agent.agent import root_agent  # 👈 or your actual agent
root_agent.mount_to_app(app)
