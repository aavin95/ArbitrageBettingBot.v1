Sports Arbitrage Betting Tool
This tool identifies arbitrage betting opportunities for NFL and NCAAF games. By comparing odds across different bookmakers, the tool determines if there's a possibility to guarantee a profit regardless of the outcome of the game.

Overview
Arbitrage betting, or "arbing", is a betting strategy where you place bets on all possible outcomes of an event at odds that guarantee a profit, regardless of the event's result. This tool automates the process of identifying such opportunities by fetching odds from various bookmakers and comparing them.

Features
Fetches and compares odds from multiple bookmakers.
Identifies arbitrage opportunities for NFL and NCAAF games.
Provides detailed logs and reports for potential betting opportunities.
Setup
Prerequisites
Python 3.x
requests library: Install using pip install requests
Configuration
Obtain an API key from OddsAPI.
Update the API_KEY variable in the config/settings.py file with your API key.
Running the Tool
Navigate to the project directory.
Run the main script:
css
Copy code
python main.py
Usage
Once the script is running, it will fetch odds for upcoming NFL and NCAAF games and identify potential arbitrage opportunities. The results will be displayed in the console.

Files
oddsapi.py: Contains the function to fetch odds data from OddsAPI.
arbitrage.py: Contains functions to identify arbitrage opportunities by comparing odds from different bookmakers.
main.py: The main script that brings everything together and runs the tool.
Limitations
The tool is limited by the data provided by the OddsAPI.
The tool does not account for betting limits, transaction fees, or other costs associated with placing bets.
Users should be aware of the risks and complexities associated with arbitrage betting.
Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

Disclaimer
This tool is for educational purposes only. Users are responsible for their own actions and decisions when using this tool. Always bet responsibly.
