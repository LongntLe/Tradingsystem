import queue, threading, yaml, logging.config
import src.trading as trading
from src.execution import Execution
from definitions import STREAM_DOMAIN, API_DOMAIN, ACCESS_TOKEN, ACCOUNT_ID
from src.risk_manager.portfolio import Portfolio
from src.strategy.randomstrategy import TestRandomStrategy
from src.streaming import StreamingForexPrices

with open('logging.yaml', 'rt') as f:
    config = yaml.safe_load(f.read())
logging.config.dictConfig(config)

logger = logging.getLogger(__name__)
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

trade_thread = threading.Thread(target=trading.trade,
                                args=(events, strategy, execution, heartbeat))  # temporarily remove portfolio

price_thread = threading.Thread(target=prices.stream_to_queue, args=[])

trade_thread.start()
price_thread.start()
