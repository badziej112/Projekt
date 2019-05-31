from _collections_abc import ABCMeta, abstractmethod

class AbstractBuilding(metaclass=ABCMeta):

    @abstractmethod
    def __init__(self, x, y, symbol):
        self.symbol = symbol
        self.x = x
        self.y = y

    @abstractmethod
    def build(self, fraction, a):
        if(fraction.material > a):
            fraction.material = fraction.material - a

    def add_building(self, fraction):
        return {self.symbol+fraction.symbol: 1}