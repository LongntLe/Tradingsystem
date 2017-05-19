class BacktestExecution(object):
    def __init__(self, equity, units, prices):
        self.equity = equity
        self.units = units
        self.price_handler = prices
    
    def execute_order(self, event):
        if event.side == "buy":
            self.units += event.units
            self.equity += event.units*self.price_handler.cur_ask
        if event.side == "sell":
            self.units += event.units
            self.equity += event.units*self.price_handler.cur_bid
        print(self.equity, self.units)
