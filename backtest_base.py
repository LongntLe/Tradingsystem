import queue
import threading
import time
from decimal import Decimal

from src.strategy.randomstrategy import TestRandomStrategy
from src.portfolio_construction.portfolio_handler import PortfolioHandler
from src.position_sizer.basic_sizer import BasicSizer
from src.risk_manager.basic_risk import BasicRiskManager
from src.price_handler.db_price_handler import DBPriceHandler
from src.backtest_execution import BacktestExecution

def trade(events, strategy, portfolio_handler, execution, heartbeat):
    while True:
        try:
            event = events.get(False)
        except queue.Empty:
            pass
        else:
            if event is not None:
                if event.type == "TICK":
                    strategy.calculate_signals(event)
                if event.type == "SIGNAL":
                    portfolio_handler.on_signal(event)
                elif event.type == "ORDER":
                    execution.execute_order(event)
        time.sleep(heartbeat)

if __name__ == "__main__":

    heartbeat = 0.0
    events = queue.Queue()
    equity = Decimal("100000.0")

    instrument = "EUR_USD"
    units = Decimal("0.0")

    prices = DBPriceHandler(
            "EUR_USD", "2015-01-01", "2016-01-01", events
            )
    
    portfolio = PortfolioHandler(equity, events, BasicSizer, BasicRiskManager)
    
    execution = BacktestExecution(equity, units, prices)

    strategy = TestRandomStrategy(instrument, units, events)

    trade_thread = threading.Thread(target=trade, args=(
        events, strategy, portfolio, execution, heartbeat))

    price_thread = threading.Thread(target=prices.stream_to_queue, args=[])

    trade_thread.start()
    price_thread.start()
