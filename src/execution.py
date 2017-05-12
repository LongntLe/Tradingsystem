import v20, logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)


class Execution(object):
    def __init__(self, domain, access_token, account_id):
        self.domain = domain
        self.access_token = access_token
        self.account_id = account_id
        self.ctx = v20.Context(
            self.domain,
            443,
            True,
            application="sample_code",
            token=self.access_token,
            datetime_format="RFC3339"
        )

    def execute_order(self, event):
        request = self.ctx.order.market(
            self.account_id,
            instrument=event.instrument,
            units=event.units
        )
        order = request.get("orderFillTransaction")
        logger.info("Transaction has been done!")
        logger.debug("%s" % order.dict())
