from _collections_abc import ABCMeta, abstractmethod

class AbstractBuilding(metaclass=ABCMeta):

    @abstractmethod
    def __init__(self, x, y, symbol):
        self.symbol = symbol
        self.x = x
        self.y = y

    def build_job(self, fraction):

        """Metoda wirtualna. Budynek wykonuje swoje zadanie."""

        pass

    def build(self, fraction): #zbudowanie budynku i odjęcie jego kosztu od materiałów frakcji

        """Metoda wirtualna. Buduje budynek."""

        pass

    def add_building(self, fraction): #dodanie symbolu budynku do mapa.show()

        """Metoda zwraca symbol budynku i frakcji."""

        return {self.symbol+fraction.symbol: 1}