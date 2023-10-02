import requests

from config.settings import API_KEY

BASE_URL = "https://api.the-odds-api.com/v4/sports/"

def get_odds(sport, regions='us', markets='h2h'):
    """Fetches odds data from OddsAPI for the specified sport and bookmakers."""

    response = requests.get(
        f'https://api.the-odds-api.com/v4/sports/{sport}/odds',
        params={
            'api_key': API_KEY,
            'regions': regions,
            'markets': markets,
            'oddsFormat': "decimal",
            'dateFormat': "iso",
        }
    )

    if response.status_code != 200:
        print(f'Failed to get odds: status_code {response.status_code}, response body {response.text}')

    else:
        odds_json = response.json()
        print('Number of events:', len(odds_json))

        # Check the usage quota
        print('Remaining requests', response.headers['x-requests-remaining'])
        print('Used requests', response.headers['x-requests-used'])
        return response.json()
