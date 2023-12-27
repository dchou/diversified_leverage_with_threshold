import os

POLYGON_CONFIG = {
    # Put your own Polygon key here:
    "API_KEY": os.environ.get("POLYGON_API_KEY"),
}

ALPACA_CONFIG = {  # Paper trading!
    # Put your own Alpaca key here:
    "API_KEY": os.environ.get("ALPACA_API_KEY"),
    # Put your own Alpaca secret here:
    "API_SECRET": os.environ.get("ALPACA_API_SECRET"),
    # If you want to use real money you must change this to False
    "PAPER": os.environ.get("ALPACA_IS_PAPER").lower() == "true",
}
