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
    # Step 1: Load existing data
    json_data = {}
    if os.path.exists(json_file):
        try:
            with open(json_file, "r") as f:
                json_data = json.load(f)
        except json.JSONDecodeError:
            print("⚠️ JSON file is corrupted or empty. Starting fresh.")
            json_data = {}

    # Step 2: Ensure all tickers exist in the data
    for ticker in nifty50_tickers:
        if ticker not in json_data:
            json_data[ticker] = []

    existing_dates = {
        ticker: {entry["Date"] for entry in json_data[ticker]}
        for ticker in nifty50_tickers
    }

    print("📥 Downloading 1 year of data...")
    data = yf.download(tickers=nifty50_tickers, period="1y", interval="1d", group_by="ticker", auto_adjust=True)

    for ticker in nifty50_tickers:
        try:
            df = data[ticker].copy()
        except KeyError:
            print(f"❌ Failed to download data for {ticker} (possibly rate limited or delisted).")
            continue

        df.reset_index(inplace=True)
        df["Date"] = df["Date"].dt.strftime("%Y-%m-%d")
        df = df[["Date", "Open", "High", "Low", "Close", "Volume"]]  # optional: trim unnecessary fields

        new_rows = df[~df["Date"].isin(existing_dates[ticker])]

        if not new_rows.empty:
            records = new_rows.to_dict(orient="records")
            json_data[ticker].extend(records)
            print(f"✅ Added {len(records)} new records for {ticker}")
        else:
            print(f"✅ {ticker} is already up to date.")

    # Step 4: Save final data
    with open(json_file, "w") as f:
        json.dump(json_data, f, indent=4)

    print("✅ Data saved to 'nifty50_data.json'")

# Call the function
if __name__ == "__main__":
    update_nifty_data()
