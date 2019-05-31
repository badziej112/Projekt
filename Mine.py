from AbstractBuilding import AbstractBuilding
import random

class Mine(AbstractBuilding):

    def __init__(self, x, y):
        super().__init__(x, y, "Mi")

    def build(self, fraction, a):
        super().build(fraction, a)

    def collect(self, fraction):
        a = random.randint(20, 80)

        fraction.material = fraction.material + a

        return a