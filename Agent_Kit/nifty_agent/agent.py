from google.adk.agents import Agent
from nifty_agent.tools.update_nifty_data import update_nifty_data
from nifty_agent.agents.visualization_agent import visualize_nifty50_chart

root_agent = Agent(
    name="nifty_root_agent",
    model="gemini-1.5-flash",
    description="Agent that manages Nifty50 data and visualization.",
    instruction="Update and show Nifty data using tools.",
    tools=[update_nifty_data, visualize_nifty50_chart],
)
