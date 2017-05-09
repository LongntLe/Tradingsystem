import abc


class PriceHandler(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def stream_to_queue(self):
        raise NotImplementedError("should implement stream_to_queue method")
