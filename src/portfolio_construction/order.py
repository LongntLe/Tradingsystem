class SuggestedOrder(object):
    def __init__(self, instrument, order_type, side, units):
        self.instrument = instrument
        self.order_type = order_type
        self.side = side
        self.units = units

