import os
from datetime import datetime
from decimal import Decimal

from dotenv import load_dotenv
from lumibot.backtesting import YahooDataBacktesting
from lumibot.entities import TradingFee
from lumibot.strategies.strategy import Strategy
from lumibot.traders import Trader

# load .env file (if one exists)
load_dotenv()

"""
Strategy Description

This strategy is loosely based on Ray Dalio's All Weather Portfolio. It will buy a diversified portfolio of leveraged assets
and rebalance the portfolio when the drift exceeds a certain threshold. The idea is that this portfolio will perform well
in all economic conditions because it is diversified across asset classes, and leveraged to increase returns.
"""

###################
# Configuration
###################

# Set to True to run the strategy live, False to backtest
IS_LIVE = os.environ.get("IS_LIVE")
# Set this to False if you want to trade with real money, or True if you want to paper trade
IS_PAPER_TRADING = os.environ.get("ALPACA_IS_PAPER")
# The date and time to start backtesting from
BACKTESTING_START = datetime(2010, 2, 15)
# The date and time to end backtesting
BACKTESTING_END = datetime(2023, 12, 19)
# The trading fee to use for backtesting
TRADING_FEE = TradingFee(percent_fee=0.001)  # Assuming 0.1% fee per trade


class DiversifiedLeverageWithThreshold(Strategy):
    # =====Overloading lifecycle methods=============

    parameters = {
        # This is the portfolio we want to own
        "portfolio": [
            {
                "symbol": "TQQQ",  # 3x Leveraged Nasdaq
                "weight": 0.20,
            },
            {
                "symbol": "UPRO",  # 3x Leveraged S&P 500
                "weight": 0.20,
            },
            {
                "symbol": "UDOW",  # 3x Leveraged Dow Jones
                "weight": 0.10,
            },
            {
                "symbol": "TMF",  # 3x Leveraged Treasury Bonds
                "weight": 0.25,
            },
            {
                "symbol": "UGL",  # 3x Leveraged Gold
                "weight": 0.10,
            },
            {
                "symbol": "DIG",  # 2x Leveraged Oil and Gas Companies (Commodities)
                "weight": 0.15,
            },
        ],
        # This is the drift threshold that will trigger a rebalance (a drift of 0.23 means 23%)
        "drift_threshold": 0.26,
    }

    def initialize(self):
        # Setting the waiting period (in days) and the counter
        self.counter = None

        # Setting the sleep time (in days) - this is the time between each trading iteration
        self.sleeptime = "1D"

        # Initializing the portfolio variable with the assets and proportions we want to own
        self.initialized = False

        self.minutes_before_closing = 1

    def on_trading_iteration(self):
        # If we exceed our drift threshold, rebalance the portfolio
        drift = self.calc_portfolio_drift()
        if drift > self.parameters["drift_threshold"]:
            self.log_message(f"Drift is {drift:.2f}, so we need to rebalance")

            self.log_message(
                f"-----------\nRebalancing portfolio because the drift is {drift:.2f}",
                broadcast=True,
            )

            self.rebalance_portfolio()
        else:
            self.log_message(
                f"Drift is only {drift:.2f}, so we don't need to rebalance"
            )

            self.log_message(
                f"-----------\nNot rebalancing portfolio because the drift is only {drift:.2f}. No action taken.",
                broadcast=True,
            )

    def calc_portfolio_drift(self, tradeable_portfolio_pct=1):
        total_portfolio_drift = Decimal(0)
        for asset in self.parameters["portfolio"]:
            # Get all of our variables from portfolio
            symbol = asset.get("symbol")
            asset_to_trade = symbol  # Asset(symbol=symbol, asset_type="stock")
            weight = asset.get("weight")
            quote = self.quote_asset
            last_price = self.get_last_price(asset_to_trade, quote=quote)

            if last_price is None:
                self.log_message(
                    f"Couldn't get a price for {symbol} self.get_last_price() returned None"
                )
                continue

            self.log_message(
                f"Last price for {symbol} is {last_price:,f}, and our weight is {weight}. Current portfolio value is {self.portfolio_value}"
            )

            # Get how many shares we already own (including orders that haven't been executed yet)
            quantity = Decimal(str(self.get_asset_potential_total(asset_to_trade)))

            # Calculate how many shares we need to buy or sell
            tradeable_portfolio_value = Decimal(
                self.portfolio_value * tradeable_portfolio_pct
            )

            current_shares_value = Decimal(last_price) * Decimal(quantity)
            current_weight = current_shares_value / tradeable_portfolio_value
            drift = Decimal(weight) - Decimal(current_weight)
            self.log_message(
                f"Current weight for {symbol} is {current_weight:.2f} and should be {weight:.2f}, so the drift is {drift*100:.2f}%"
            )

            total_portfolio_drift += abs(drift)

        self.log_message(f"Total portfolio drift is {total_portfolio_drift:.2f}")
        return float(total_portfolio_drift)

    # ============= Helper Methods ====================

    def rebalance_portfolio(self):
        """Rebalance the portfolio and create orders"""

        orders = []
        for asset in self.parameters["portfolio"]:
            # Get all of our variables from portfolio
            symbol = asset.get("symbol")
            weight = asset.get("weight")
            last_price = self.get_last_price(symbol)

            # Get how many shares we already own (including orders that haven't been executed yet)
            position = self.get_position(symbol)
            quantity = 0
            if position is not None:
                quantity = float(position.quantity)

            # Calculate how many shares we need to buy or sell
            shares_value = self.portfolio_value * weight
            self.log_message(
                f"The current portfolio value is {self.portfolio_value} and the weight needed is {weight}, so we should buy {shares_value}"
            )
            new_quantity = shares_value // last_price
            quantity_difference = new_quantity - quantity
            self.log_message(
                f"Currently own {quantity} shares of {symbol} but need {new_quantity}, so the difference is {quantity_difference}"
            )

            # If quantity is positive then buy, if it's negative then sell
            side = ""
            if quantity_difference > 0:
                side = "buy"
            elif quantity_difference < 0:
                side = "sell"

            # Calculate the percentage of the portfolio that this order represents
            pct_of_portfolio = (quantity_difference * last_price) / self.portfolio_value

            # If the percentage is less than 1% then don't execute the order
            if abs(pct_of_portfolio) < 0.01:
                self.log_message(
                    f"Skipping {symbol} because the percentage of the portfolio is only {pct_of_portfolio*100:.2f}%"
                )
                continue

            # Execute the order if necessary
            if side:
                order = self.create_order(symbol, abs(quantity_difference), side)
                orders.append(order)

        # Submit all the sell orders first (to free up cash)
        for order in orders:
            if order.side == "sell":
                self.submit_order(order)

        # Sleep for 15 seconds to make sure the sell orders are executed
        self.sleep(15)

        # Then submit all the buy orders
        for order in orders:
            if order.side == "buy":
                self.submit_order(order)


if __name__ == "__main__":
    # Convert the string to a boolean.
    # This will be True if the string is "True", and False otherwise.
    is_live = IS_LIVE.lower() != "false"

    if is_live:
        ####
        # Live Trading
        ####
        from credentials import ALPACA_CONFIG
        from lumibot.brokers import Alpaca

        trader = Trader()
        broker = Alpaca(ALPACA_CONFIG)
        strategy = DiversifiedLeverageWithThreshold(broker)

        trader.add_strategy(strategy)
        strategies = trader.run_all()

    else:
        ####
        # Backtest the strategy
        ####

        # Initialize the backtesting object
        print("Starting Backtest...")
        DiversifiedLeverageWithThreshold.backtest(
            YahooDataBacktesting,
            BACKTESTING_START,
            BACKTESTING_END,
            benchmark_asset="SPY",
            buy_trading_fees=[TRADING_FEE],
            sell_trading_fees=[TRADING_FEE],
        )
