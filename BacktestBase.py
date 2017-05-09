class BacktestBase(object):
    def __init__(
            self, symbol, start, end,
            amount, ftc=0.0, ptc=0.0
    ):
        self.symbol = symbol
        self.start = start
        self.end = end
        self._amount = amount
        self.amount = amount
        self.ftc = ftc
        self.ptc = ptc
        self.units = 0
        self.position = 0
        self.trades = 0
        self.fullreport = True
        self.get_data()
        # TODO: get command line input

    def get_data(self):
        # Retrieve price from source
        pass

    def plot_data(self):
        # Plot data and save it to plots folder
        self.data["price"].plot(figsize=(10, 6), title=self.symbol + " from " + self.start + " to " + self.end)

    def print_balance(self, date=' '):
        pass

    def get_bar(self, bar):
        # Return timestamp and price for bar
        pass

    def place_buy_order(self, bar, units=None, amount=None):
        # Place a buy order
        pass

    def place_sell_order(self, bar, units=None, amount=None):
        # Place a sell order
        pass

    def close_position(self, bar):
        # close out a position
        pass
