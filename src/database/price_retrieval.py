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
config.read('pyalgo.cfg')
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
suffix = '.000000000Z'

def flatten_dict(d):
    def items():
        for key, value in d.items():
            if isinstance(value, dict):
                for subkey, subvalue in flatten_dict(value).items():
                    yield key + '.' + subkey, subvalue
            else:
                return key, value
    return dict(items())

def get_data(instrument: str, start_date: str, end_date: str):
    instrument = instrument
    start_date = dt.datetime.strptime(start_date, "%Y-%m-%d %H:%M:%S")
    end_date = dt.datetime.strptime(end_date, "%Y-%m-%d %H:%M:%S")
    # dateTime formatting
    d1 = start_date.isoformat('T') + suffix
    limit = end_date.isoformat('T') + suffix

    # data chunking
    prices = pd.DataFrame()
    dates = pd.date_range(start=d1, end=limit, freq='D')
    for i in range(len(dates) - 1):
        d1 = str(dates[i]).replace(' ', 'T')
        d2 = str(dates[i + 1]).replace(' ', 'T')
        candle = ctx.instrument.candles(
            instrument=instrument,
            fromTime=d1,
            toTime=d2,
            granularity='S10',
            price='MBA' 
        )
        data = candle.get('candles')
        data = [flatten_dict(cs.dict()) for cs in data]  # turn data into dict, pretty important
        
        Kappa = pd.DataFrame(data)
        prices = prices.append(Kappa)

        # translate the data into dictionary and pandas DataFrame

        # create dataframe
        # prices = pd.DataFrame(data)
    print("data downloaded successfully")
    prices["time"] = pd.to_datetime(prices["time"])
    prices = prices.set_index("time")
    prices.index = pd.DatetimeIndex(prices.index)
    prices.to_hdf("./database/%s.h5" % instrument, "data", format="table")
    print("data imported to file")
