from __future__ import absolute_import

import logging
import queue
import threading
import time

from definitions import STREAM_DOMAIN, API_DOMAIN, ACCESS_TOKEN, ACCOUNT_ID
from src.price_handler.streaming import StreamingForexPrices
from src.portfolio_construction.portfolio_handler import PortfolioHandler
from src.position_sizer.basic_sizer import BasicSizer
from src.risk_manager.basic_risk import BasicRiskManager
from src.strategy.randomstrategy import TestRandomStrategy
from src.execution import Execution

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)


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
                elif event.type == "SIGNAL":
                    portfolio_handler.on_signal(event)
                elif event.type == "ORDER":
                    logger.info("Executing order")
                    execution.execute_order(event)
        time.sleep(heartbeat)


def main():
    logger.info("Trading Algorithm has started!")
    heartbeat = 0.5
    events = queue.Queue()

    instrument = "EUR_USD"
    units = 10000

    prices = StreamingForexPrices(
        STREAM_DOMAIN, ACCESS_TOKEN, ACCOUNT_ID,
        instrument, events
    )

    portfolio = PortfolioHandler(100000.0, events, BasicSizer, BasicRiskManager)  # TODO: decimal, dynamic

    execution = Execution(API_DOMAIN, ACCESS_TOKEN, ACCOUNT_ID)

    strategy = TestRandomStrategy(instrument, units, events)

    trade_thread = threading.Thread(target=trade, args=(events, strategy, portfolio, execution, heartbeat))

    price_thread = threading.Thread(target=prices.stream_to_queue, args=[])

    trade_thread.start()
    price_thread.start()
