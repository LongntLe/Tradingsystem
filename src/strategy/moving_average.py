from __future__ import absolute_import
from src.event import OrderEvent
import pandas as pd
import numpy as np

class MAstrat(object):
	def __init__(self, instrument, units, events):
        self.instrument = instrument
        self.units = units
        self.events = events
        self.ticks = 0
        self.data = pd.DataFrame()

    def initialize(self, event):
        self.position = 0
        if event.type == "TICK":
            self.ticks += 1
            self.data = self.data.append(
                pd.DataFrame({"ticks": [self.ticks], "time": [event.time], "ask": [event.ask]}))
            self.data.index = pd.DatetimeIndex(self.data["time"])
            resam = self.data.resample("5S").last()
        return resam

    def calculate_signal(self, event, weight): # weight is the weight matrix
    	self.position = 0
        if event.type == "TICK":
            self.ticks += 1
            self.data = self.data.append(
                pd.DataFrame({"ticks": [self.ticks], "time": [event.time], "ask": [event.ask]}))
            self.data.index = pd.DatetimeIndex(self.data["time"])
            resam = self.data.resample("5S").last()
        
        length = weight.shape[0]
        resam["returns"] = np.log(resam["ask"] / resam["ask"].shift(1))
        ma = resam["returns"].rolling(length)*np.transpose(weight)
        resam["position"] = np.sign(resam["ask"]-ma) # moving average

        if resam["position"].ix[-1] == 1:  # last position is higher than previous means
                if self.position == 0:  # position of portfolio equals to 0 => buy because no transaction happens before that
                    order = OrderEvent(
                        self.instrument, self.units, "market", "buy"
                    )
                elif self.position == -1:
                    order = OrderEvent(
                        self.instrument, 2 * self.units, "market", "buy"  # order buy happens when
                    )
                else:
                    order = OrderEvent(
                        self.instrument, 0, "market", "buy"
                    )
                self.position = 1
                self.events.put(order)
            elif resam["position"].ix[-1] == -1:
                if self.position == 0:
                    order = OrderEvent(
                        self.instrument, -self.units, "market", "sell"
                    )
                elif self.position == 1:
                    order = OrderEvent(
                        self.instrument, -2 * self.units, "market", "sell"
                    )
                else:
                    order = OrderEvent(
                        self.instrument, 0, "market", "buy"
                    )
                self.position = -1
                self.events.put(order)

    def control(self,event): # determining when to short vs when to long
    	pass
