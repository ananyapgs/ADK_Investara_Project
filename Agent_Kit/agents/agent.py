from datetime import datetime
from google.adk.agents import Agent
from google.adk.tools import google_search


root_agent = Agent(
    name="stock_market_guide_agent",
    model="gemini-2.0-flash",
    description="An assistant that helps beginners get started with the stock market.",
    instruction="""
    Greet the user and ask their name.
    Mention that you are a financial assistant who can help with stock market basics.
    Use tools like:
    - google_search to find live answers and tutorials.
    Do not mention which are the tools you are using while interacting with user
    """,
)
