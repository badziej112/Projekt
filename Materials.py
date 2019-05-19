from _collections_abc import ABCMeta, abstractmethod

class AbstractMaterial(metaclass=ABCMeta):

    @abstractmethod
    def __init__(self,number, typename, position,symbol):
        self.number = number
        self.typename = typename
        self.position = position
        self.symbol = symbol
    def generate(self):
        pass
