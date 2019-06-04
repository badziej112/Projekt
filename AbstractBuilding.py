from _collections_abc import ABCMeta, abstractmethod

class AbstractBuilding(metaclass=ABCMeta):

    @abstractmethod
    def __init__(self, x, y, symbol):
        self.symbol = symbol
        self.x = x
        self.y = y

    @abstractmethod
    def build(self, fraction, a): #zbudowanie budynku i odjęcie jego kosztu od materiałów frakcji
        if(fraction.material > a):
            fraction.material = fraction.material - a

    def add_building(self, fraction): #dodanie symbolu budynku do mapa.show()
        return {self.symbol+fraction.symbol: 1}