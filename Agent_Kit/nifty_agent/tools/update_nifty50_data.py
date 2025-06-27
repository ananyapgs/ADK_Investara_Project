import yfinance as yf
import json
import os
import pandas as pd
from typing import List
from nifty_agent.constants import nifty50_tickers

def update_nifty50_data(tickers: List[str] = []) -> str:
    json_file = "nifty_agent/data/nifty_data.json"

    # Always use fixed Nifty 50 tickers
    tickers = nifty50_tickers
    tickers_str = " ".join(tickers)

    # Load existing data if available
    if os.path.exists(json_file):
        with open(json_file, "r") as f:
            json_data = json.load(f)
    else:
        json_data = {}

    # Ensure all tickers have an initialized list
    for ticker in tickers:
        if ticker not in json_data:
            json_data[ticker] = []

    # Get existing dates per ticker to avoid duplicates
    existing_dates = {
        ticker: {entry["Date"] for entry in json_data[ticker]}
        for ticker in tickers
    }

    # Download 1 year of data for all tickers
    data = yf.download(tickers_str, period="1y", interval="1d", group_by="ticker", auto_adjust=True)

    updated_tickers = []

    for ticker in tickers:
        # Handle single-ticker case
        if len(tickers) == 1 and not isinstance(data.columns, pd.MultiIndex):
            df = data.copy()
        elif isinstance(data.columns, pd.MultiIndex) and ticker in data.columns.get_level_values(0):
            df = data[ticker].copy()
        else:
            continue  # Skip if no data

        df = df.reset_index()
        df["Date"] = df["Date"].dt.strftime("%Y-%m-%d")

        # Keep only new rows not already in JSON
        new_rows = df[~df["Date"].isin(existing_dates[ticker])]

        if not new_rows.empty:
            json_data[ticker].extend(new_rows.to_dict(orient="records"))
            updated_tickers.append(ticker)

    # Save updated JSON
    with open(json_file, "w") as f:
        json.dump(json_data, f, indent=4)

    if updated_tickers:
        return f"✅ Appended new data for: {', '.join(updated_tickers)}"
    else:
        return "✅ All tickers were already up to date."
