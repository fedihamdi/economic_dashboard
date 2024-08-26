import sys
import os

# Add the root directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import schedule
import time
from data.fetch_data import get_economic_data
from db.database import store_data_to_sqlite


def update_data():
    df = get_economic_data()
    store_data_to_sqlite(df, "economic_indicators")


def start_scheduler():
    schedule.every().day.at("00:00").do(update_data)

    while True:
        schedule.run_pending()
        time.sleep(1)
