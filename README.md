# Documentation

## Onboarding

Welcome to the team! Please first read the following document to gain a good understanding about our trading system.

### Basic knowledge

- Basic finance terminologies, [Investopedia](http://www.investopedia.com) is your bestfriend.
Read definitions on Investopedia and do a brief research before asking.
- Watch the following [video](https://ocw.mit.edu/courses/mathematics/18-s096-topics-in-mathematics-with-applications-in-finance-fall-2013/video-lectures/lecture-1-introduction-financial-terms-and-concepts/) from MIT opencourseware
- Basic knowledge in calculus, statistics and probability.
In the future, we may work on stochastic calculus and differential equations.
Experience in math modeling is recommended.
- Documents will be given to people working on specific areas. Contact Hoang and Long for more details.

### What we do
As we are yet to have an official name, we will refer to this system as "Tradingsystem".
Tradingsystem is an algorithmic trading system,
but we don't limit ourselves to quant as we also do technical analysis and fundamentals analysis.
At the moment, we are trading forex and we may expand to stocks and derivatives in the future.  

Algorithmic trading is an extremely rewarding academic-wise.
We have several projects in software engineering, economics, finance mathematics and machine learning
for everyone to work on.
Here, we have [a list of open tasks](https://docs.google.com/spreadsheets/d/1BJZxA-PRkMm2HwMaKohUK1VaKiOfIIbV8SNgL5QiMrU/edit#gid=0).

## Infrastructure Description: 
Our system mostly uses Python 2. It is advised for newcomers to have good knowledge in Python and feel comfortable in using GitHub. 

### Threads:
1. `streaming.py`: output - real time EURUSD price from Oanda as TICK events (check `event.py`) 
2. `strategy.py`: analyze TICK events to determine when to enter. Output is SIGNAL events.

### Strategies:
See strategy folder. There are three main strategies:
- Mean-reversion
- Momentum
- Moving averages

### Risk management:
1. `portfolio.py`: receive SIGNAL events - conduct risk management. Output - ORDER event. (under dev)

### Simulation - Backtesting:
Expectation: modify `strategy.py` --> `strategy_session.py`. User could choose to backtest or trade live. 
We would import `BacktestBase.py`, which is under development. The expected output is statistical indicators of strategy's performance. 

`hist.py`: download historical data for analysis and building backtests. 

### Evaluation:
`statisticaltest.py`: statistical analysis to evaluate strategy's performance. 

## Dependencies
Python 2.7. PyPy JIT Compiler 5.8.0.

All required packages are listed in `requirements.txt`.

## Installation

These software/packages must be installed in sequence.
We haven't prepare documentation for Windows users.

### Oracle Java Development Kit 8

#### Ubuntu
Visit [here](https://www3.ntu.edu.sg/home/ehchua/programming/howto/JDK_Howto.html) for more details.
#### macOS
- Install [HomeBrew](https://brew.sh).
- `$ brew cask install java`
- Open file `~/.bash_profile` and add these two lines:
```bash
export JAVA_HOME=/Library/Java/JavaVirtualMachines/1.x.x_xxx-bxx
export PATH=$JAVA_HOME/bin:$PATH
```

### Apache Cassandra

- Download Cassandra [here](http://cassandra.apache.org/download/).
Unzip the downloaded file.
- Open `~/.bash_profile` (on macOS) or `~/.bashrc` (on Ubuntu).
- Add these two lines:
```bash
alias cassandra='p/a/t/h/apache-cassandra-x.xx/bin/cassandra'
alias cqlsh='p/a/t/h/apache-cassandra-x.xx/bin/cqlsh'
```
- Activate the alias by restarting Terminal or `source ~/.bashrc` (Ubuntu) or `source ~/.bash_profile` (macOS).
### PyPy
- Download PyPy for Python 2.7 [here](http://pypy.org/download.html).
### VirtualEnv
- `$ [sudo] pip install virtualenv`
- **Inside** the folder `Tradingsystem`, run `$ virtualenv -p p/a/t/h/pypy2-v.5.71-osname/bin/pypy venv`.

## Contribution

- Fork this repository to your own GitHub account.
- Download the project to your machine: `$ git clone https://github.com/username/Tradingsystem`
- Follow the installation guidance.
- Get it run:
```bash
$ source venv/bin/activate
(Tradingsystem) $ pip install -r requirements.txt
$ cassandra
$ python __main__.py
```

## Other
Contact long.le@minerva.kgi.edu and hoang.nguyen@minerva.kgi.edu for more details. Task distribution will be according to project list google sheets file.
