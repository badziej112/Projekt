from AbstractBuilding import AbstractBuilding

class City(AbstractBuilding):

    def __init__(self, x, y, population):

        super().__init__(x, y, "C")
        self.population = population

    def build(self, fraction):

        """Buduje miasto i odejmuje jego koszt od zasobów frakcji oraz dodaje punkty rozwoju."""

        if (fraction.material > 1000):
            fraction.material = fraction.material - 1000
            fraction.points += 100

    def build_job(self, fraction):

        """Konsumpcja jedzenia frakcji przez miasto. Przyrost/redukcja populacji w zależności od
        ilości posiadanego jedzenia."""

        if (fraction.food > (self.population * 2)):
            fraction.food = fraction.food - (self.population * 1.5)
            self.population = self.population * 1.5
        elif (fraction.food >= (self.population)):
            fraction.food = fraction.food - self.population
            self.population = self.population * 1.2
            return False
        elif (fraction.food < self.population): #głód
            self.population = self.population * 0.7
            return True


