import os

POLYGON_CONFIG = {
    # Put your own Polygon key here:
    "API_KEY": os.environ.get("POLYGON_API_KEY"),
    "IS_PAID_SUBSCRIPTION": os.environ.get("POLYGON_IS_PAID_SUBSCRIPTION").lower()
    == "true"
    if os.environ.get("POLYGON_IS_PAID_SUBSCRIPTION")
    else False,
}

ALPACA_CONFIG = {  # Paper trading!
    # Put your own Alpaca key here:
    "API_KEY": os.environ.get("ALPACA_API_KEY"),
    # Put your own Alpaca secret here:
    "API_SECRET": os.environ.get("ALPACA_API_SECRET"),
    # If you want to use real money you must change this to False
    "PAPER": os.environ.get("ALPACA_IS_PAPER").lower() == "true"
    if os.environ.get("ALPACA_IS_PAPER")
    else True,
}
