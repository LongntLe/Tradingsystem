# Documentation


## Infra Description: 

### Authorization:
settings.py + pyalgo.cfg: to access trading account. 

Two main threads:
1. streaming.py: output - real time EURUSD price from Oanda as TICK events (check event.py) 
2. strategy.py: analyze TICK events to determine when to enter. output - SIGNAL events.

### Strategies:
See strategy folder. There are three main strategies
- Mean-reversion
- Momentum
- Moving averages

### Risk management:
1. portfolio.py: receive SIGNAL event - conduct risk management. Output - ORDER event. (under dev)

### Simulation - Backtesting:
Expectation: modify strategy.py --> strategy_session.py. User could choose to backtest or trade live. 
Would import BacktestBase.py (under dev): output: statistical indicators of strategy's performance. 
new_hist.py: download historical data for analysis and building backtests. 

### Evaluation:
statisticaltest.py: output - statistical analysis to evaluate strategy's performance. 

Note on Oanda API: http://developer.oanda.com/rest-live-v20/introduction/
- Must connect using Context method. i.e ctx.Connect(args)


## Dependencies
Python 3.5.12 (therefore remember to install Python 3 dependencies)

### API used:
### Core APIs
- numpy
```
pip3 install numpy
```
- pandas
```
pip3 install pandas
```
- scipy
```
pip3 install scipy
```
- queue
```
pip3 install queuelib
```
- time
### Broke APIs
- Oanda
```
pip3 install Oanda
```
### Risk managing and strategy developing APIs
- portfolioopt (has a variety of risk management tools)
```
pip3 install portfolioopt
```
- statsmodels (for statistics indicators)
```
pip3 install statsmodels
```
- johansen (Johansen test)
```
pip3 install johansen
```

### Other
- threading
- seaborn (for data visualization)

## Other
Contact long.le@minerva.kgi.edu and hoang.nguyen@minerva.kgi.edu for more details. Task distribution will be according to project list google sheets file.
