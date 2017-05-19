from __future__ import absolute_import
from src.price_handler.price_handler import PriceHandler
from src.price_handler.price_handler import PriceHandler
from src.event import TickEvent
import pandas as pd

from decimal import Decimal, ROUND_HALF_DOWN

"""
experimental event-based streaming system:
    stream all datapoints from a file 
    for ONLY ONE instrument
"""
    #TODO: mutiple pairs
    #TODO: set a start date and an end date
class DBPriceHandler(PriceHandler):
    def __init__(self, instrument, start_date, end_date, events):
        self.instrument = instrument
        self.start_date = start_date
        self.end_date = end_date
        self.events_queue = events
        #temporarily del db_dir and events_queue
        self.cur_bid = None
        self.cur_ask = None

    def _retrieve_prices(self):
        return pd.read_hdf("src/database/data.h5", columns=["time","ask.o","mid.o","bid.o"])

    def stream_to_queue(self):
        self.price_pool = self._retrieve_prices()
        for row in range(len(self.price_pool)):
            self.cur_bid = Decimal(self.price_pool.iloc[row]["ask.o"]).quantize(
                    Decimal("0.00001"), ROUND_HALF_DOWN
                    )
            self.cur_ask = Decimal(self.price_pool.iloc[row]["bid.o"]).quantize(
                    Decimal("0.00001"), ROUND_HALF_DOWN
                    )
            tev = TickEvent(self.instrument, self.price_pool.index[row], self.cur_bid, self.cur_ask)
            self.events_queue.put(tev)
