import pandas as pd

import datetime as dt
import v20

import configparser

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pylab

# new_hist.py

config = configparser.ConfigParser()
config.read('../pyalgo.cfg')
access_token = config['oanda_v20']['access_token']

# v20.context
ctx = v20.Context(
    'api-fxpractice.oanda.com',
    443,
    True,
    application='sample_code',
    token=config['oanda_v20']['access_token'],
    datetime_format='RFC3339'
)

response = ctx.account.instruments(config['oanda_v20']['account_id'])
r = response.get('instruments')

# dateTime formatting
suffix = '.000000000Z'
time1 = dt.datetime(2015, 1, 15, 8, 0, 0)
d1 = time1.isoformat('T') + suffix
# time2 = dt.datetime(2016,8,2,0,0,0)
# d2 = time2.isoformat('T') + suffix
# time_unit = dt.timedelta(1)
limit = dt.datetime(2015, 1, 16, 16, 0, 0)
limit = limit.isoformat('T') + suffix

# data chunking
prices = pd.DataFrame()
dates = pd.date_range(start=d1, end=limit, freq='D')
for i in range(len(dates) - 1):
    d1 = str(dates[i]).replace(' ', 'T')
    d2 = str(dates[i + 1]).replace(' ', 'T')
    candle = ctx.instrument.candles(
        instrument='EUR_USD',
        fromTime=d1,
        toTime=d2,
        granularity='S5',
        price='MBA'
    )
    data = candle.get('candles')
    data = [cs.dict() for cs in data]  # turn data into dict, pretty important
    for cs in data:
        cs.update(cs['ask'])
        del cs['ask']
    Kappa = pd.DataFrame(data)
    prices = prices.append(Kappa)

    # translate the data into dictionary and pandas DataFrame

    # create dataframe
    # prices = pd.DataFrame(data)
print(prices)
prices["time"] = pd.to_datetime(prices["time"])
prices = prices.set_index("time")
prices.index = pd.DatetimeIndex(prices.index)
prices.to_hdf("data.h5", "data", format="table")
