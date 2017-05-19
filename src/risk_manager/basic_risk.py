from src.risk_manager.risk_base import RiskManager
from src.event import OrderEvent

class BasicRiskManager(RiskManager):
    def __init__(self):
        pass
    
    def refine_order(self, sized_order):
        order = OrderEvent(
                sized_order.instrument,
                sized_order.units,
                sized_order.order_type,
                sized_order.side
                )
        return order
