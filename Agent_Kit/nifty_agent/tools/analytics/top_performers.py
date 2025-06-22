import os
import json
import pandas as pd
from nifty_agent.constants import nifty50_tickers

def get_top_performers(n: int = 5) -> str:
    json_file = "nifty_agent/data/nifty_data.json"
    if not os.path.exists(json_file):
        return "❌ Data file not found."

    with open(json_file, "r") as f:
        json_data = json.load(f)

    results = []
    for ticker, records in json_data.items():
        if not records:
            continue
        try:
            latest = sorted(records, key=lambda x: x["Date"])[-1]
            open_price = float(latest["Open"])
            close_price = float(latest["Close"])
            change_pct = round(((close_price - open_price) / open_price) * 100, 2)
            results.append({"Ticker": ticker, "Change %": change_pct})
        except Exception:
            continue

    if not results:
        return "⚠️ No valid data found."

    top = sorted(results, key=lambda x: x["Change %"], reverse=True)[:n]

    return "📈 Top Gainers:\n" + "\n".join(f"{r['Ticker']}: {r['Change %']}%" for r in top)
