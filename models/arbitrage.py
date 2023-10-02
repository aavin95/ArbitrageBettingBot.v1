from itertools import combinations
from api.oddsapi import get_odds

def get_odds_for_bookmaker(event, bookmaker):
    """Extracts the odds for a specific bookmaker from an event's data."""
    for site in event['sites']:
        if site['site_key'] == bookmaker:
            # Assuming 'odds' key contains odds data, and 'h2h' key contains head-to-head odds
            return site['odds']['h2h']
    return None

def find_arbitrage(odds1, odds2):
    """Checks if there's an arbitrage opportunity between two odds."""
    prob1 = 1 / odds1[0]
    prob2 = 1 / odds2[1]
    total_prob = prob1 + prob2

    return total_prob < 1

def check_arbitrage_for_sport(sport, bookmakers):
    """Checks for arbitrage opportunities for a sport among multiple bookmakers."""
    odds_data = get_odds(sport, ",".join(bookmakers))
    
    if not odds_data:
        print(f"Failed to fetch odds data for {sport}.")
        return
    
    # Loop through all games/events
    for event in odds_data['data']:
        # Loop through all combinations of bookmakers
        for book1, book2 in combinations(bookmakers, 2):
            team1_odds_book1 = get_odds_for_bookmaker(event, book1)
            team2_odds_book2 = get_odds_for_bookmaker(event, book2)
            
            if not team1_odds_book1 or not team2_odds_book2:
                continue  # Skip if odds data is missing for any bookmaker
            
            if find_arbitrage(team1_odds_book1, team2_odds_book2):
                print(f"Arbitrage opportunity found between {book1} and {book2} for {event['teams'][0]['name']} vs {event['teams'][1]['name']} in {sport}!")
