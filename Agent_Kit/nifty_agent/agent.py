from google.adk.agents import Agent
from nifty_agent.tools import update_nifty50_data, visualize_nifty50_data
from nifty_agent.tools.analytics.top_performers import get_top_performers
from nifty_agent.tools.analytics.top_losers import get_top_losers
from nifty_agent.tools.analytics.bullish_bearish import get_candle_sentiment

root_agent = Agent(
    name="nifty_agent",
    model="gemini-2.0-flash",
    description="Agent that manages Nifty50 data and visualization.",
    instruction="""
    You automatically update and visualize Nifty 50 stock data using Yahoo Finance.
    Always use the predefined list of stock symbols from constants.py (nifty50_tickers) when calling `update_nifty50_data` and `visualize_nifty50_data`.

    You can also answer questions like:
    - Who are the top gainers?
    - Who are the top losers?
    - Which stock performed best today?
    - Which stocks are showing bullish or bearish candles?

    Use the Nifty50 data stored in JSON format to answer such analytics questions using the appropriate tool.
    """,
    tools=[
        update_nifty50_data,
        visualize_nifty50_data,
        get_top_performers,
        get_top_losers,
        get_candle_sentiment
    ],
)
