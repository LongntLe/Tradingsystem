from src.portfolio_construction.order import SuggestedOrder

class PortfolioHandler(object):
    def __init__(self, equity, events, position_sizer, risk_manager):
        self.equity = equity
        self.positions = {}
        self.events = events
        self.position_sizer = position_sizer
        self.risk_manager = risk_manager
        #self.margin_used = 0
        #self.margin_available = 0

    def create_order_from_signal(self, signal_event):
        initial_order = SuggestedOrder(
                signal_event.instrument,
                signal_event.order_type,
                signal_event.side,
                signal_event.units
                )
        return initial_order

    def on_signal(self, signal_event):
        initial_order = self.create_order_from_signal(signal_event)
        sized_order = self.position_sizer().size_order(initial_order)
        final_order = self.risk_manager().refine_order(sized_order)
        self.events.put(final_order)

