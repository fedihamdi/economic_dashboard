from data.fetch_data import get_economic_data
from db.database import store_data_to_sqlite
from visualization.dashboard import create_dashboard
from scheduler.update_scheduler import start_scheduler

if __name__ == "__main__":
    # Fetch data and store it
    df = get_economic_data()
    store_data_to_sqlite(df, "economic_indicators")

    # Start the dashboard
    create_dashboard()

    # Start the scheduler to update data periodically
    start_scheduler()
