import os
import requests
import json
from datetime import datetime
import time
from config.logging_config import setup_logging
import logging

API_KEY = os.getenv("WEATHER_API_KEY")

setup_logging()
logger = logging.getLogger(__name__)

if not API_KEY:
    logging.error("API KEY not set")
    SystemExit(1)

india_cities = [
    "Delhi", "Mumbai", "Bangalore", "Chennai", "Hyderabad", "Kolkata",
    "Pune", "Ahmedabad", "Jaipur", "Chandigarh", "Noida", "Gurgaon",
    "Faridabad", "Ghaziabad", "Lucknow", "Kanpur", "Indore", "Bhopal",
    "Nagpur", "Surat", "Vadodara", "Rajkot", "Udaipur",
    "Kochi", "Trivandrum", "Thrissur", "Coimbatore", "Madurai",
    "Trichy", "Salem", "Erode",
    "Vijayawada", "Visakhapatnam", "Guntur",
    "Warangal", "Nizamabad",
    "Patna", "Gaya", "Muzaffarpur",
    "Ranchi", "Jamshedpur", "Dhanbad",
    "Bhubaneswar", "Cuttack", "Rourkela",
    "Guwahati", "Silchar",
    "Shillong", "Imphal", "Aizawl",
    "Agra", "Mathura", "Meerut", "Aligarh",
    "Dehradun", "Haridwar", "Rishikesh",
    "Shimla", "Manali", "Dharamshala",
    "Jammu", "Srinagar", "Leh"
]

international_cities = [
    # UK & Europe
    "London", "Manchester", "Birmingham", "Edinburgh",
    "Paris", "Lyon", "Marseille",
    "Berlin", "Munich", "Frankfurt",
    "Amsterdam", "Rotterdam",
    "Madrid", "Barcelona",
    "Rome", "Milan",
    "Zurich", "Geneva",

    # USA & Canada
    "New York", "Los Angeles", "San Francisco", "Seattle",
    "Chicago", "Boston", "Austin", "Dallas",
    "Toronto", "Vancouver", "Montreal",

    # Middle East
    "Dubai", "Abu Dhabi", "Doha", "Riyadh", "Jeddah",

    # Asia-Pacific
    "Singapore", "Kuala Lumpur", "Bangkok",
    "Jakarta", "Manila",
    "Tokyo", "Osaka", "Kyoto",
    "Seoul", "Busan",
    "Hong Kong",
    "Shanghai", "Beijing", "Shenzhen",
    "Sydney", "Melbourne", "Brisbane",
    "Auckland"
]


cities = india_cities + international_cities

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
    for city in cities:
        data = fetch_weather(city)
        time.sleep(1)

        if not data:
            logger.error("No data is fetched")
        else:
            save_raw_data(data, city)

    

if __name__ == "__main__":
    main()
    