from tools.update_nifty_data import update_nifty_data
from agents.visualization_agent import visualize_nifty50_chart
from agents.visualization_agent import visualization_agent

if __name__ == "__main__":
    print("🔁 Updating data...")
    update_nifty_data()

    print("📊 Running visualization agent...")
    response = visualize_nifty50_chart()
    print(response)
