from __future__ import absolute_import

import logging
import queue
import threading
import time
from definitions import STREAM_DOMAIN, API_DOMAIN, ACCESS_TOKEN, ACCOUNT_ID
from src.price_handler.streaming import StreamingForexPrices
from src.risk_manager.portfolio import Portfolio
from src.strategy.randomstrategy import TestRandomStrategy
from src.execution import Execution

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

def trade(events, strategy, execution, heartbeat):  # temporarily remove portfolio
    while True:
        try:
            event = events.get(False)
        except queue.Empty:
            pass
        else:
            if event is not None:
                if event.type == "TICK":
                    strategy.calculate_signals(event)
                # elif event.type == "SIGNAL":
                #    portfolio.execute_signal(event)
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

    portfolio = Portfolio(prices, events, equity=100000.0)  # TODO: decimal, dynamic

    execution = Execution(API_DOMAIN, ACCESS_TOKEN, ACCOUNT_ID)

    strategy = TestRandomStrategy(instrument, units, events)

    trade_thread = threading.Thread(target=trade,
                                    args=(events, strategy, execution, heartbeat))  # temporarily remove portfolio

    price_thread = threading.Thread(target=prices.stream_to_queue, args=[])

    trade_thread.start()
    price_thread.start()
