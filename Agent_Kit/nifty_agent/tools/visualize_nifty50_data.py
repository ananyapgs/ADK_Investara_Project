import matplotlib.pyplot as plt
import json
import pandas as pd
import os
from typing import List  # ✅ ADD THIS
from nifty_agent.constants import nifty50_tickers

def visualize_nifty50_data(tickers: List[str] = []) -> str:
    json_file = "nifty_agent/data/nifty_data.json"
    tickers = nifty50_tickers

    if not os.path.exists(json_file):
        return "❌ Data file not found. Please run update_nifty50_data first."

    with open(json_file, "r") as f:
        json_data = json.load(f)

    missing = [ticker for ticker in tickers if ticker not in json_data]
    if missing:
        return f"⚠️ No data for: {', '.join(missing)}. Please run update first."

    plt.figure(figsize=(12, 6))
    for ticker in tickers:
        df = pd.DataFrame(json_data[ticker])
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

    image_path = "nifty_agent/data/nifty50_plot.png"
    plt.savefig(image_path)
    plt.close()

    return f"✅ Chart saved to {image_path}"
