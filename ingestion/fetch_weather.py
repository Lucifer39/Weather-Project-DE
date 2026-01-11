import os
import requests
import json
from datetime import datetime
import time
from config.logging_config import setup_logging
import logging
from config.cities import ALL_CITIES

API_KEY = os.getenv("WEATHER_API_KEY")

setup_logging()
logger = logging.getLogger(__name__)
cities = ALL_CITIES

if not API_KEY:
    logging.error("API KEY not set")
    SystemExit(1)

def fetch_weather(city):
    logger.info(f"Fetching data started for {city}...")
    url="https://api.weatherapi.com/v1/current.json"
    params = {
        "q": city,
        "key": API_KEY
    }

    response = requests.get(url, params=params, timeout=10)
    
    if response.status_code == 200:
        logger.info(f"Fetching data successful for {city}.")
        return response.json()
    elif response.status_code == 401:
        logger.error("Invalid API key")
    elif response.status_code == 429:
        logger.warning("Rate limit hit, backing off")
    elif response.status_code >= 500:
        logger.error("Weather API server error")
    else:
        logger.error(
            f"Failed to fetch weather | city={city} | "
            f"status={response.status_code} | response={response.text}"
        )

        return None
    
def save_raw_data(weather_data, city):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    os.makedirs("storage/raw", exist_ok=True)
    path = f"storage/raw/weather_rawdata_{city}_{timestamp}.json"

    logger.info(f"Saving data to {path}...")
    with open(path, "w",) as f:
        json.dump(weather_data, f, indent=2)

    logger.info(f"Saved data to {path}.")

def main():
    total_cities = len(cities)
    success = 0
    failed = 0
    for idx, city in enumerate(cities, start=1):
        data = fetch_weather(city)
        time.sleep(1)

        if not data:
            failed += 1
            logger.error(f"[{idx}/{total_cities}] FAILED | city = {city}")
        else:
            save_raw_data(data, city)
            success += 1
            logger.info(f"[{idx}/{total_cities}] SUCCESS | city = {city}")
    
    logger.info(f"Task completed | {success} success | {failed} failed")

    

if __name__ == "__main__":
    main()
    