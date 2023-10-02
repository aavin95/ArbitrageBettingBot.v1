from itertools import combinations
from api.oddsapi import get_odds

def get_odds_for_bookmaker(event, bookmaker):
    """Extracts the odds for a specific bookmaker from an event's data."""
    for bookie in event['bookmakers']:
        if bookie['key'] == bookmaker:
            outcomes = bookie['markets'][0]['outcomes']
            odds = []
            # Ensure odds are in the order of home_team and away_team
            for team in [event['home_team'], event['away_team']]:
                for outcome in outcomes:
                    if outcome['name'] == team:
                        odds.append(outcome['price'])
            return odds
    return None

def find_arbitrage(odds1, odds2):
    """Checks if there's an arbitrage opportunity between two odds."""
    prob1 = 1 / odds1[0]
    prob2 = 1 / odds2[1]
    total_prob = prob1 + prob2
    return total_prob < 1

def check_arbitrage_for_sport(sport):
    """Checks for arbitrage opportunities for a sport among multiple bookmakers."""
    odds_data = get_odds(sport, 'us', 'h2h')

    if not odds_data:
        print(f"Failed to fetch odds data for {sport}.")
        return
    arbitrage_found = False
    # Loop through all games/events
    for event in odds_data:
        # Get all bookmakers for the current event
        bookmakers_for_event = [bookie['key'] for bookie in event['bookmakers']]

        # Loop through all combinations of bookmakers for the current event
        for book1, book2 in combinations(bookmakers_for_event, 2):
            team1_odds_book1 = get_odds_for_bookmaker(event, book1)
            team2_odds_book2 = get_odds_for_bookmaker(event, book2)

            if not team1_odds_book1 or not team2_odds_book2:
                continue  # Skip if odds data is missing for any bookmaker
            if find_arbitrage(team1_odds_book1, team2_odds_book2):
                arbitrage_found = True
                print(f"Arbitrage opportunity found between {book1} and {book2} for {event['home_team']} vs {event['away_team']} in {sport}!")
    if arbitrage_found is False:
        print("No arbitrage opportunities found")