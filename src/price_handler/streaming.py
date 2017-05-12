from src.price_handler.price_handler import PriceHandler
from src.event import TickEvent
import v20
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)


class StreamingForexPrices(PriceHandler):
    def __init__(
            self, domain, access_token,
            account_id, instruments, events_queue
    ):
        # self.ticks = 0
        # self.data = pd.DataFrame()
        self.domain = domain
        self.access_token = access_token
        self.account_id = account_id
        self.instruments = instruments
        self.events_queue = events_queue
        self.cur_bid = None
        self.cur_ask = None
        self.ctx_stream = v20.Context(
            self.domain,
            443,
            True,
            application="sample_code",
            token=self.access_token,
            datetime_format="RFC3339"
        )

    def stream_to_queue(self):
        response = self.ctx_stream.pricing.stream(
            self.account_id,
            snapshot=True,
            instruments=self.instruments
        )
        for msg_type, msg in response.parts():
            if msg_type == "pricing.Price":
                logger.info('Received a tick! %s %s %s %s' %
                            (msg.instrument, msg.time, msg.asks[0].price, msg.bids[0].price))
                instrument = msg.instrument
                time = msg.time
                bid = msg.bids[0].price
                ask = msg.asks[0].price
                tev = TickEvent(instrument, time, bid, ask)
                self.events_queue.put(tev)
                self.cur_bid = bid
                self.cur_ask = ask
            elif msg_type == "pricing.Heartbeat":
                print(msg)
