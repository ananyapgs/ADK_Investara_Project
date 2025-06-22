import os
import json
from nifty_agent.constants import nifty50_tickers

def get_candle_sentiment() -> str:
    json_file = "nifty_agent/data/nifty_data.json"
    
    if not os.path.exists(json_file):
        return "❌ Data file not found."

    with open(json_file, "r") as f:
        json_data = json.load(f)

    result = []
    
    for ticker, records in json_data.items():
        if not records:
            continue
        try:
            latest = sorted(records, key=lambda x: x["Date"])[-1]
            open_price = float(latest["Open"])
            close_price = float(latest["Close"])

            if close_price > open_price:
                sentiment = "📈 Bullish"
            elif close_price < open_price:
                sentiment = "📉 Bearish"
            else:
                sentiment = "⚖️ Doji"

            result.append(f"{ticker}: {sentiment}")
        except Exception:
            continue

    if not result:
        return "⚠️ No valid data found to determine candle sentiment."

    return "📊 Candle Sentiment (Latest Day):\n" + "\n".join(result)
