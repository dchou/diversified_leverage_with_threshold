# Disclaimer

This strategy and the accompanying code are provided for educational purposes only and are not intended to be used with real money or as investment advice. They are meant to be used as tools for financial analysis and should not be the sole basis for any investment decisions. Lumiwealth is not a licensed investment advisor.

1. Hypothetical Performance: Any backtesting results presented are hypothetical and do not represent actual trading. Past performance is not indicative of future results. There is no guarantee that the strategy will perform similarly in the future, nor is there any assurance of profitability.

2. User Risk: The strategy and code may not be suitable for your specific financial situation and risk tolerance. It is crucial to consult with a qualified financial professional before making any investment decisions.

3. Code Warranty: The code is provided 'as is' without any warranty. While efforts have been made to ensure its correctness, Lumiwealth does not guarantee that the code is free from bugs or errors.

4. Information Accuracy: All accompanying information, including strategy descriptions, backtests, etc., is provided without warranty and may be subject to errors or inaccuracies. Lumiwealth reserves the right to make changes to the code and information at any time without notice.

5. License: For detailed licensing information, please refer to the [license](LICENSE).

6. Scope of Agreement: This disclaimer is specific to the strategy and code in question and does not supersede the broader Terms of Service agreed upon during the Lumiwealth signup process. It is an integral part of the larger legal framework governing your use of Lumiwealth's services.

By using this strategy and code, you acknowledge and agree to the terms outlined in this disclaimer, which form part of the agreement between you and Lumiwealth.

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
| IS_BACKTESTING    | Set to "True" to run the strategy in backtesting mode, set to "False" to run the strategy live (defaults to False) | False                                  |

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

