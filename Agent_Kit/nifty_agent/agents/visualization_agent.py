from google.adk.agents import Agent
from datetime import datetime
import matplotlib.pyplot as plt
import pandas as pd
import json
import os

# Tool function
def visualize_nifty50_chart():
    json_file = "nifty50_data.json"
    if not os.path.exists(json_file):
        return "The data file doesn't exist. Please run the data update process first."

    with open(json_file, "r") as f:
        json_data = json.load(f)

    tickers = ['RELIANCE.NS', 'TCS.NS', 'HDFCBANK.NS', 'ICICIBANK.NS', 'KOTAKBANK.NS']
    plt.figure(figsize=(12, 6))
    for ticker in tickers:
        df = pd.DataFrame(json_data.get(ticker, []))
        if df.empty:
            continue
        df["Date"] = pd.to_datetime(df["Date"])
        plt.plot(df["Date"], df["Close"], label=ticker)

    plt.title("Nifty 50 - Closing Prices Over 1 Year")
    plt.xlabel("Date")
    plt.ylabel("Close Price (INR)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    return "Here's the latest visualization of Nifty 50 stock prices."

# Define the agent
visualization_agent = Agent(
    name="visualization_agent",
    model="gemini-2.0-flash",
    description="An agent that visualizes Nifty 50 stock data.",
    instruction="""
    You are a data visualization assistant. When the user asks to see stock trends,
    load the latest available Nifty 50 stock data from a local file and generate a line chart showing the closing prices.
    Do not mention what tools or files you're using.
    Provide the chart and a friendly summary.
    """,
    tools=[visualize_nifty50_chart]  # ✅ Correct format
)
