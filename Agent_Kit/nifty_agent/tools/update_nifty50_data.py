import yfinance as yf
import json
import os
import pandas as pd
from typing import List
from nifty_agent.constants import nifty50_tickers

def update_nifty50_data(tickers: List[str] = []) -> str:
    json_file = "nifty_agent/data/nifty_data.json"

    tickers = nifty50_tickers  # Always use fixed tickers

    if os.path.exists(json_file):
        with open(json_file, "r") as f:
            json_data = json.load(f)
    else:
        json_data = {}

    for ticker in tickers:
        if ticker not in json_data:
            json_data[ticker] = []

    existing_dates = {
        ticker: {entry["Date"] for entry in json_data[ticker]}
        for ticker in tickers
    }

    data = yf.download(" ".join(tickers), period="1y", group_by="ticker", interval="1d")
    updated_tickers = []

    for ticker in tickers:
        if len(tickers) == 1 and not isinstance(data.columns, pd.MultiIndex):
            df = data.copy()
        elif ticker in data.columns.levels[0]:
            df = data[ticker].copy()
        else:
            continue

        df.reset_index(inplace=True)
        df["Date"] = df["Date"].dt.strftime("%Y-%m-%d")
        new_rows = df[~df["Date"].isin(existing_dates[ticker])]

        if not new_rows.empty:
            json_data[ticker].extend(new_rows.to_dict(orient="records"))
            updated_tickers.append(ticker)

    with open(json_file, "w") as f:
        json.dump(json_data, f, indent=4)

    if updated_tickers:
        return f"✅ Updated data for: {', '.join(updated_tickers)}"
    return "✅ All tickers were already up to date."
