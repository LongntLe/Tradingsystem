import numpy as np
import pandas as pd
from pandas_datareader import data as web

# implement by chapter 4 in pyalgoquant

# we will get data from 2002 to test

#data = new_hist.export() # retrieve historical data
lookback = [1,5,10,25,60,120]
holddays = [1,5,10,25,60,120]
transcost = []

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

class MomentumVectBacktest(object):
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
		self.data = raw

	def run_strategy(self, momentum = 1):
		self.momentum = momentum # probably the sign
		data = self.data.copy()
		data['position'] = np.sign(data['returns'].rolling(m).mean())
		data['strategy'] = data['position'].shift(1)*data['returns']
		# determine when a trade takes place

	def momentumsign(data, ticks):
		if self.results is None:
			print('No result to plot yet')
		

	def plot_results(self):
		pass

