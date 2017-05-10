import sys
sys.path.insert(0, '../database')

import numpy as np
import pandas as pd
from pandas_datareader import data as web

import new_hist

# implement by chapter 4 in pyalgoquant

# we will get data from 2002 to test

#data = new_hist.export() # retrieve historical data
lookback = [1,2,5,10]
holddays = [1,5,10,25,60,120]
tcost = [0, 0.001, 0.002, 0.003, 0.004, 0.005] # transaction cost

'''
data = web.DataReader('AAPL', data_source='yahoo',end='2016-10-31')['Adj Close'] #get data, could be anything
data = pd.DataFrame(data)

data.rename(columns={'Adj Close': 'price'}, inplace=True)

data['returns'] = np.log(data['price']/data['price'].shift(1)) #gets growth rate

data['position'] = np.sign(data['returns']) # identify the direction of momentum
data['strategy'] = data['position'].shift(1)*data['returns']
data[['returns','strategy']].dropna().cumsum().apply(np.exp).plot(figsize=(10,6)) # plotting cumulative returns of the time series

to_plot = ['returns']

for m in ticks:
	data['position_%d' % m] = np.sign(data['returns'].rolling(m).mean())
	data['strategy_%d' % m] = data['position_%d' % m].shift(1)*data['returns']
	to_plot.append('strategy_%d' % m)
'''
# temporary obsolette




class MomVectBacktest(object):
	def __init__(self, symbol, start, end, amount, tc):
		self.symbol = symbol
		self.start = start # start date
		self.end = end # end date
		self.amount = amount # amount to be invested initially
		self.tc = tc # transaction costs
		self.results = None
		self.get_data()

	def get_data(self): #fetching data, this uses yahoo data, but we may use other
		raw = web.DataReader(self.symbol, data_source='yahoo',start=self.start, end=self.end)['Adj Close']
		raw = pd.DataFrame(raw)
		raw.rename(columns={'Adj Close': 'price'}, inplace=True)
		raw['return'] = np.log(raw/raw.shift(1))
		np.sign(raw['return']) # get the position
		self.data = raw # get raw data

	def get_data_Oanda(self): # will get data from new_hist.py
		self.data = new_hist.export()

	def run_strategy(self, momentum = 1):
		self.momentum = momentum
		data = self.data.copy()
		data['position'] = np.sign(data['return'].rolling(momentum).mean()) # get momentum
		data['strategy'] = data['position'].shift(1)*data['return'] # order buy or sell with the quantity of return
		# determine when a trade takes place
		trades = data['position'].diff().fillna(0) != 0
		# subtract transaction costs from return when trade takes place
		data['strategy'][trades] -= self.tc # for each trade, subtract tcost
		data['creturns'] = self.amount * data['return'].cumsum().apply(np.exp) # take cumsum of return?
		data['cstrategy'] = self.amount * data['strategy'].cumsum().apply(np.exp)
		self.results = data
		# absolute performance of the strategy
		aperf = self.results['cstrategy'].ix[-1]
		# out-/underperformance of strategy
		operf = aperf - self.results['creturns'].ix[-1]
		return round(aperf, 2), round(operf, 2)

	def plot_results(self):
		if self.results is None:
			print('No result to plot yet')
		title = '%s | TC = %.4f' % (self.symbol, self.tc)
		self.results[['creturns','cstrategy']].plot(title=title,figsize=(10,6))

if __name__ == '__main__':
	for t in range(len(lookback)):
		print('lookback period %d' %lookback[t])
		for i in range(len(tcost)):
			mombt = MomVectBacktest('AAPL','2010-1-1','2016-10-31',10000, tcost[i])
			print(mombt.run_strategy(momentum=lookback[t]))


'''
A few notes:
- First we need to determine the sign of the momentum, the easiest way to do this was
to get the sign of the return, but we can also get the sign of m latest return, therefore,
we use rolling(m)
- m here can be understood as lookback period? Is there another way to model lookback period?

Will need to learn how to plot stuff

'''

