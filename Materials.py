from _collections_abc import ABCMeta, abstractmethod

class AbstractMaterial(metaclass=ABCMeta):

    @abstractmethod
    def __init__(self,number, symbol):
        self.number = number
        self.symbol = symbol
    def generate(self):
        pass
