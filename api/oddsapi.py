# oddsapi.py
import requests
from config.settings import API_KEY

BASE_URL = "https://api.the-odds-api.com/v3/"

def get_odds(sport, bookmakers):
    """
    Fetches the odds for a given sport from specified bookmakers.
    
    Parameters:
        sport (str): The name of the sport to fetch odds for.
        bookmakers (str): Comma-separated string of bookmakers to fetch odds from.
        
    Returns:
        dict: A dictionary containing the odds data or None if an error occurs.
    """
    endpoint = f"{BASE_URL}odds/?apiKey={API_KEY}&sport={sport}&bookmaker={bookmakers}&oddsFormat=decimal"
    response = requests.get(endpoint)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching odds: {response.status_code}")
        return None

# You can add more functions here for other OddsAPI endpoints or functionalities as needed.
