# poker-call-option
>This module uses a monte carlo simulation to analyze the payoff structure of poker tournaments by using option valuation methods.
## Description
This is a fun little project I created to better understand how to exploit the payoff structure of poker tournaments. When compared to cash games, poker tournament payoffs resemble a call option. You pay a premium to join and your payoff is derived from your ranking. The interesting quirk about this structure is that it assumes you are an X% ranked player (the X is what this simulation will try and derive). If you are ranked >X% then you can *arbitrage* the tournament generating positive EV in the long run. The "strike price" in this case is fixed at X. The only caveat is that while your mean ranking might be greater than X%, it is difficult to consistently place in the same ranking. Therefore, the variance will be high and you might have many tournaments in a row where you lose your premium.

## optimization_x.py
This script is used to back out the breakeven X%. In other words, out of all players, if you rank in the X% percentile, you will breakeven. If you are better than X%, you will make money in the long run.
