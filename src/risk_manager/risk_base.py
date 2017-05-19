import abc

class RiskManager(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def refine_order(self, sized_order):
        raise NotImplementedError("should implement refineorder()")
