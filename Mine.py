from AbstractBuilding import AbstractBuilding
import random

class Mine(AbstractBuilding):

    def __init__(self, x, y):

        super().__init__(x, y, "Mi")

    def build(self, fraction):

        """Buduje kopalnie i odejmuje jego koszt od zasobów frakcji oraz dodaje punkty rozwoju."""

        if (fraction.material > 500):
            fraction.material = fraction.material - 500
            fraction.points += 50

    def build_job(self, fraction):

        """Wygenerowanie losowej ilości materiałów i zebranie jej."""

        a = random.randint(20, 250)
        fraction.material = fraction.material + a
        return a