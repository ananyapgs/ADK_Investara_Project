from google.adk.agents import Agent
from nifty_agent.tools import update_nifty50_data, visualize_nifty50_data

root_agent = Agent(
    name="nifty_agent",
    model="gemini-2.0-flash",
    description="Agent that manages Nifty50 data and visualization.",
    instruction="""
    You automatically update and visualize Nifty 50 stock data using Yahoo Finance.
    Always use the predefined list of stock symbols from constants.py (nifty50_tickers) when calling `update_nifty50_data` and `visualize_nifty50_data`.
    The user does not need to provide the stock symbols. Use the default list internally to fetch and chart data over the last 1 year.
    You can also use the data which is there in `nifty_data.json` and answer the question which user asks
    """,
    tools=[update_nifty50_data, visualize_nifty50_data],
)
