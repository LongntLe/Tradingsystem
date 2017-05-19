from src.position_sizer.base import PositionSizer

class BasicSizer(PositionSizer):
    
    def size_order(self, initial_order):
        if initial_order.side == "buy":
            initial_order.units = 1000
        elif initial_order.side == "sell":
            initial_order.units = -1000
        else:
            print("nope")
        return initial_order
