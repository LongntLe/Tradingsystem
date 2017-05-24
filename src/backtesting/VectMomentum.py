from __future__ import division, absolute_import

import numpy as np
import pandas as pd
from pandas_datareader import data as web

import matplotlib.pyplot as plt

import sys

sys.path.insert(0, '../statistics/')

import statisticaltest as stat  # importing MDD, Hurst

sys.path.insert(0, '../../')

import hist

# implement by chapter 4 in pyalgoquant

# we will get data from 2002 to test

# data = new_hist.export() # retrieve historical data
symbol = ['AAPL', 'EUR=X']
forex = ['AUD=X', 'CAD=X', 'CHF=X', 'CNY=X', 'EUR=X', 'GBP=X', 'JPY=X', 'SGD=X', 'USD=X']
lookback = [5, 10, 25, 50]
holddays = [1, 5, 10, 25, 60, 120]
tcost = [0, 0.00005]  # transaction cost

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
		# will add Oanda data here, use data['ask.o']
		# raw = hist.data_export()
		raw = web.DataReader(self.symbol, data_source='yahoo',start=self.start, end=self.end)['Adj Close']
		raw = pd.DataFrame(raw)
		raw.rename(columns={'Adj Close': 'price'}, inplace=True)
		raw['return'] = np.log(raw/raw.shift(1))
		np.sign(raw['return']) # get the position
		self.data = raw # get raw data

	def run_strategy(self, momentum = 1):
		self.momentum = momentum
		data = self.data.copy()
		data['position'] = np.sign(data['return'].rolling(momentum).mean()) # generate position dataframe by rolling data points
		data['strategy'] = data['position'].shift(1)*data['return']
		# determine when a trade takes place
		trades = data['position'].diff().fillna(0) != 0
		# subtract transaction costs from return when trade takes place
		data['strategy'][trades] -= self.tc
		data['creturns'] = self.amount * data['return'].cumsum().apply(np.exp)
		data['cstrategy'] = self.amount * data['strategy'].cumsum().apply(np.exp)
		self.results = data
		# absolute performance of the strategy
		aperf = self.results['cstrategy'].ix[-1]
		# out-/underperformance of strategy
		operf = aperf - self.results['creturns'].ix[-1]
		return round(aperf, 2), round(operf, 2), round(stat.hurst(data['price']), 4), round(self.MDD(data['cstrategy']), 4)

	def MDD(self, data): # calculating maximum drawdown
		MDD = 0
		peak = self.amount
		trough = self.amount

		for i in range(len(data)):
			if (peak < data[i]):
				peak = data[i]
				trough = data[i]
			elif (trough > data[i]):
				trough = data[i]

			MDD = min(MDD, (trough-peak)/peak)
		return MDD

	def plot_results(self):
		if self.results is None:
			print('No result to plot yet')
		title = '%s | TC = %.5f' % (self.symbol, self.tc)
		self.results[['creturns','cstrategy']].plot(title=title,figsize=(10,6))
		plt.show()
to_plot = ['returns']


if __name__ == '__main__':
    for t in range(len(lookback)):
        print('lookback period %d' % lookback[t])
        for i in range(len(tcost)):
            mombt = MomVectBacktest(forex[5], '2005-01-01', '2011-01-01', 10000, tcost[i])  # object
            print(mombt.run_strategy(momentum=lookback[t]))

'''
A few notes:
- First we need to determine the sign of the momentum, the easiest way to do this was
to get the sign of the return, but we can also get the sign of m latest return, therefore,
we use rolling(m)
- m here can be understood as lookback period? Is there another way to model lookback period?

Will need to learn how to plot stuff (resolved)

EURUSD symbol seems to be bugged (resolved)
'''
