from event import OrderEvent
import pandas as pd
import numpy as np

lookback = [1, 5, 10, 25, 60, 120]
holddays = [1, 5, 10, 25, 60, 120]


def past_returns():
    '''
    pseudocode:
    - indicates time-series momentum
    -
    '''


pass


def alex_filter(self, event):
    self.position = 0
    if event.type == "TICK":
        self.ticks += 1
        self.data = self.data.append(
            pd.DataFrame({"ticks": [self.ticks], "time": [event.time], "ask": [event.ask]}))
        self.data.index = pd.DatetimeIndex(self.data["time"])
        resam = self.data.resample("5S").last()
