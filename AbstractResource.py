from _collections_abc import ABCMeta, abstractmethod

class AbstractResource(metaclass=ABCMeta):

    @abstractmethod
    def __init__(self, symbol):
        self.symbol = symbol



