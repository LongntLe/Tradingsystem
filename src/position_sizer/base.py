import abc

class PositionSizer(metaclass=abc.ABCMeta):
    def __init__(self):
        pass
    @abc.abstractmethod
    def size_order(self, initial_order):
        raise NotImplementedError("should implement size_order()")

