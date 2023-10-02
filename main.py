# Assuming these imports are at the top of your file
from models.arbitrage import check_arbitrage_for_sport

def main():
    sports = ["americanfootball_nfl", "americanfootball_ncaaf"]
    bookmakers = ["bet365", "ladbrokes", "bovada", "betfair", "draftkings"]

    for sport in sports:
        check_arbitrage_for_sport(sport)

if __name__ == "__main__":
    main()

