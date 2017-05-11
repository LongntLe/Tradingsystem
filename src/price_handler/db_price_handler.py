import price_handler
import price_retrieval
import os.path
import pandas as pd


class DBPriceHandler(PriceHandler):
    def __init__(self, instrument, start_date, end_date, events_queue, db_dir):
        self.instrument = instrument
        self.start_date = start_date
        self.end_date = end_date
        self.events_queue = events_queue
        self.db_dir = db_dir
        self.cur_bid = None
        self.cur_ask = None

    def _retrieve_prices(self):
        if os.path.isfile("%s.h5" % self.instrument) == "False":
            price_retrieval.get_data(self.instrument, self.start_date, self.end_date)

        else:
            pd.read_hdf("%s.h5" % self.instrument)

    def stream_to_queue(self):
        self.retrieve_prices()
        for index, row in self
