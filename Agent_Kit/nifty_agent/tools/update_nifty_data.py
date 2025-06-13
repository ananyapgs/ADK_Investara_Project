import yfinance as yf
import json
import os
from datetime import datetime
import pandas as pd

json_file = "nifty50_data.json"

nifty50_tickers = [
    'RELIANCE.NS', 'TCS.NS', 'HDFCBANK.NS', 'ICICIBANK.NS', 'KOTAKBANK.NS'
]

def update_nifty_data():
    if os.path.exists(json_file):
        with open(json_file, "r") as f:
            json_data = json.load(f)
    else:
        json_data = {}

    for ticker in nifty50_tickers:
        if ticker not in json_data:
            json_data[ticker] = []

    existing_dates = {
        ticker: {entry["Date"] for entry in json_data[ticker]}
        for ticker in nifty50_tickers
    }

    print("📥 Downloading 1 year of data...")
    data = yf.download(" ".join(nifty50_tickers), period="1y", group_by="ticker", interval="1d")

    for ticker in nifty50_tickers:
        df = data[ticker].copy()
        df.reset_index(inplace=True)
        df["Date"] = df["Date"].dt.strftime("%Y-%m-%d")
        new_rows = df[~df["Date"].isin(existing_dates[ticker])]

        if not new_rows.empty:
            records = new_rows.to_dict(orient="records")
            json_data[ticker].extend(records)
            print(f"✅ Added {len(records)} new records for {ticker}")
        else:
            print(f"✅ {ticker} is already up to date.")

    with open(json_file, "w") as f:
        json.dump(json_data, f, indent=4)

    print("✅ Data saved to 'nifty50_data.json'")
