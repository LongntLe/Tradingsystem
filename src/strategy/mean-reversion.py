from __future__ import absolute_import
from src.event import OrderEvent
import pandas as pd
import numpy as np
from src.statistics.statisticaltest import hurst  # calculating hurst exponent

'''
Strategy note:
To do:
    - How to take different ticks
        - calculate hurst as test first, can get historical data
    - How ADF tests


'''
tick_distance = "5S"


class meanrevertstrat(object):
    def __init__(self, instrument, units, events):
        self.instrument = instrument
        self.units = units
        self.events = events
        self.ticks = 0
        self.data = pd.DataFrame()

    def calculate_signals(self, event):
        lookback = 20  # look back period length
        self.position = 0
        if event.type == "TICK":
            self.ticks += 1
            self.data = self.data.append(
                pd.DataFrame({"ticks": [self.ticks], "time": [event.time], "ask": [event.ask]}))
            resam = self.data.resample(tick_distance).last()
        resam["returns"] = np.log(resam["ask"] / resam["ask"].shift(1))

    pass


def linearMR():
    lookback = halflife  # The look-back for the moving average and standard deviation can be set to equal the half-life.
    pass
