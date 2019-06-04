from AbstractBuilding import AbstractBuilding
import random

class Mine(AbstractBuilding):

    def __init__(self, x, y):
        super().__init__(x, y, "Mi")

    def build(self, fraction, a): #abstract
        super().build(fraction, a)

    def collect(self, fraction): #randomowe zebranie materiałów, tu chyba bez pogody
        a = random.randint(10, 200)
        fraction.material = fraction.material + a
        return a