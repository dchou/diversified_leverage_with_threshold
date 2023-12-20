# Disclaimer

This strategy is for educational purposes only. It is not intended to be investment advice or to be used with real money, use at your own risk. Any backtesting results are hypothetical and do not represent actual trading. There is no guarantee that the strategy will perform as well in the future as it did in the past, and there is no guarantee that it will be profitable in the future. Furthermore, the strategy may not be appropriate for your financial situation and risk tolerance. You should not make any investment decisions based solely on what you read here as it is not a substitute for professional investment advice and the backtests may contain errors.

Furthermore, the code here is given as is without any warranty. While the code is believed to be correct, there is no guarantee that it is free of bugs or errors. All information below (such as the strategy description, backtest, etc) is given as is without any warranty, and may be incorrect. The code and information below may be changed at any time without notice.

For more information see the [license](LICENSE).

This disclaimer and license supercedes anything else you may have heard or read about this strategy or code, including anything on the Lumiwealth website, social media, or elsewhere. Regardless of what you may have heard or read elsewhere, this disclaimer and license is the only valid and binding agreement between you and Lumiwealth regarding this strategy and code. If you do not agree with this disclaimer and license, you must not use this strategy or code.

# Strategy Description

This strategy is loosely based on Ray Dalio's All Weather Portfolio. It will buy a diversified portfolio of leveraged assets
and rebalance the portfolio when the drift exceeds a certain threshold. The idea is that this portfolio will perform well
in all economic conditions because it is diversified across asset classes, and leveraged to increase returns.

# Installation

To run this strategy on Replit you need to click the "Run on Repl.it" button below and fill in your secret keys in the replit secrets tab. 
 
### TIP: Right click on the button and open it in a new tab so that you can see the instructions while you are setting up the strategy (otherwise you will have to press the back button to see the instructions again).

[![Run on Repl.it](https://replit.com/badge/github/Lumiwealth-Strategies/diversified_leverage_with_threshold)](https://replit.com/new/github/Lumiwealth-Strategies/diversified_leverage_with_threshold)

# Configuration

The strategy can be configured by setting the following secrets in the replit secrets tab. Inside replit, just open the secrets tab (under tools) and click "New secret" to add a new secret. The secret key should be the name of the secret (from the left column in the table below) and the secret value should be the value of the secret depending on your situation (example values are given in the right column in the table below).

If you are running the strategy on your own computer, you can set these as environment variables.

| Secret            | Description                                                                                   | Example                                 |
|-------------------|-----------------------------------------------------------------------------------------------|-----------------------------------------|
| ALPACA_API_KEY    | Your API key from your Alpaca brokerage account                                               | PK7T6YVAX6PMH1EM20YN                    |
| ALPACA_API_SECRET | Your secret key from your Alpaca brokerage account                                            | 9WgJLS3wIXq54FCpHwwZjCp8JCfJfKuwSrYskKMA |
| ALPACA_IS_PAPER   | Set to "True" to use the Alpaca paper trading API, set to "False" to use the Alpaca real money trading API | True                                  |
| IS_LIVE           | Set to "True" to run the strategy live, set to "False" to run the strategy in backtesting mode | False                                  |

# Modifying the Parameters

The strategy parameters can be modified by editing the "parameters" section of the code, usually near the top of the file just under the class defeinition. It is a python dictionary that looks like this:

```python
parameters = {
    "my_parameter_1": 1,
    ...
}
```

You can change the values of the parameters by editing the numbers in the dictionary. For example, if you wanted to change the value of "my_parameter_1" to 2, you would change the code to look like this:

```python
parameters = {
    "my_parameter_1": 2,
    ...
}
```

Each parameter controls a different aspect of the strategy, and the description of each parameter is given next to the parameter in the code. Changing the parameters can have a big effect on the performance of the strategy, so it is recommended that you backtest the strategy after changing the parameters to see how it performs.

# Backtest

This is a backtest of the strategy using the current parameters in the code. Remember that past performance is not indicative of future results and there is no guarantee that the backtest was performed correctly or that the strategy will perform without errors when run live.

![Tearsheet generated by QuantStats](Tearsheet%20(generated%20by%20QuantStats).jpg)

