# Documentation

## Onboarding

Welcome to the team! Please first read the following document to gain a good understanding about our trading system.

### Basic knowledge

- About basic finance terminologies, investopedia is your bestfriend. Read the definition on investopedia and do a brief research before asking.
- Watch the following video from MIT opencourseware https://ocw.mit.edu/courses/mathematics/18-s096-topics-in-mathematics-with-applications-in-finance-fall-2013/video-lectures/lecture-1-introduction-financial-terms-and-concepts/
- About mathematics, newcomers should have basic knowledge in calculus, statistics and probability. In the future, we may work on stochastic calculus and differential equations. Experience in math modeling is recommended.
- Specific documents will be given to people working on specific areas. Contact Hoang and Long for more details.

### What we do
As we are yet to have an official name, we will refer to this system as "tradingsystem". Tradingsystem is basically an algorithmic trading system, but we don't limit ourselves to quant as we also do technical analysis and fundamentals analysis. At the moment, we are trading forex and we may expand to stocks and derivatives in the future.  

Algorithmic trading is an extremely rewarding academic-wise. We have several projects in software engineering, economics, finance mathematics and machine learning for everyone to work on. Here, we have a list of open projects https://docs.google.com/spreadsheets/d/1BJZxA-PRkMm2HwMaKohUK1VaKiOfIIbV8SNgL5QiMrU/edit#gid=0

## Infra Description: 
Our system mostly uses Python 3. It is advised for newcomers to have good knowledge in Python and feel comfortable in using GitHub.

### Authorization:
settings.py + pyalgo.cfg: to access trading account. 

Two main threads:
1. streaming.py: output - real time EURUSD price from Oanda as TICK events (check event.py) 
2. strategy.py: analyze TICK events to determine when to enter. output - SIGNAL events.

### Strategies:
See strategy folder. There are three main strategies:  
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

### Broker APIs
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
