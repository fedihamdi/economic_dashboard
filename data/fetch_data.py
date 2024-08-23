import os

import requests
import pandas as pd
import logging
from dotenv import load_dotenv

load_dotenv()

# Initialize logging
logging.basicConfig(
    filename='fendi_ai.log',
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
)
logger = logging.getLogger(__name__)

API_URL = "https://api.tradingeconomics.com/historical/country/mexico/indicator/Interest Rate"
logger.info("Fetch API ...")
API_KEY = os.getenv("API_KEY")

def get_economic_data():
    response = requests.get(API_URL, params={"c": API_KEY})
    logger.info("Chat history downloaded by the user.")

    data = response.json()
    logger.info(f"Connection is secured {response}")

    df = pd.DataFrame(data)  # Convert to DataFrame
    return df
