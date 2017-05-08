# Documentation


## Infra Description: 

### Authorization:
settings.py + pyalgo.cfg: to access trading account. 

Two main threads:
1. streaming.py: output - real time EURUSD price from Oanda as TICK events (check event.py) 
2. strategy.py: analyze TICK events to determine when to enter. output - SIGNAL events.

### Strategies:
See strategy folder

### Risk management:
1. portfolio.py: receive SIGNAL event - conduct risk management. Output - ORDER event. (under dev)

### Simulation - Backtesting:
Expectation: modify strategy.py --> strategy_session.py. User could choose to backtest or trade live. 
would import BacktestBase.py (under dev): output: statistical indicators of strategy's performance. 
new_hist.py: download data for analysis and building backtests. 

### Evaluation:
statisticaltest.py: output - statistical analysis to evaluate strategy's performance. 

Note on Oanda API: http://developer.oanda.com/rest-live-v20/introduction/
- Must connect using Context method. i.e ctx.Connect(args)


### Dependencies
Python 3.5.12 (therefore remember to install Python 3 dependencies)

API used:
- numpy
```
pip3 install numpy
```
- pandas
```
pip3 install pandas
```
- Oanda
```
pip3 install Oanda
```
- scipy
```
pip3 install scipy
```
- statsmodels
```
pip3 install statsmodels
```
- queue
```
pip3 install queuelib
```
- time
- threading
And so on.