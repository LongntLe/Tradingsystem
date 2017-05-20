import pandas as pd

import datetime as dt
import v20

import configparser

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pylab

from definitions import ACCESS_TOKEN, ACCOUNT_ID
#new_hist.py

#v20.context
ctx = v20.Context(
        'api-fxpractice.oanda.com',
        443,
        True,
        application='sample_code',
        token = ACCESS_TOKEN,
        datetime_format='RFC3339'
        )

response = ctx.account.instruments(ACCOUNT_ID)
r = response.get('instruments')

def flatten_dict(d):
    def items():
        for key, value in d.items():
            if isinstance(value, dict):
                for subkey, subvalue in flatten_dict(value).items():
                    yield key + "." + subkey, subvalue
            else:
                yield key, value
    return dict(items())
#dateTime formatting
suffix = '.000000000Z'
time1 = dt.datetime(2008,12,10,0,0,0)
d1 = time1.isoformat('T') + suffix
limit = dt.datetime(2009,10,10,0,0,0)
limit = limit.isoformat('T') + suffix

#data chunking
prices = pd.DataFrame()
dates = pd.date_range(start = d1, end = limit, freq = 'D')
for i in range(len(dates)-1):
    d1 = str(dates[i]).replace(' ', 'T')
    d2 = str(dates[i+1]).replace(' ', 'T')
    candle = ctx.instrument.candles(
            instrument = 'EUR_USD',
            fromTime = d1,
            toTime = d2,
            granularity = 'S10',
            price = 'MBA'
            )
    data = candle.get('candles')
    data = [flatten_dict(cs.dict()) for cs in data] #turn data into dict, pretty important

    print(data)
    Kappa = pd.DataFrame(data)
    prices = prices.append(Kappa)
        #translate the data into dictionary and pandas DataFrame

        #create dataframe    
#print("data downloaded")
prices["time"] = pd.to_datetime(prices["time"])
prices = prices.set_index("time")
prices.index = pd.DatetimeIndex(prices.index)
prices.to_hdf("src/database/data_5.h5", "data", format="table")
    
print("imported data to file\n", pd.HDFStore("src/database/data_5.h5"))