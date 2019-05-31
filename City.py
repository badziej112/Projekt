from AbstractBuilding import AbstractBuilding

class City(AbstractBuilding):

    def __init__(self, x, y):
        super().__init__(x, y, "C")
        self.population = 10
        self.level = 1

    def consume(self, fraction): # konsumpcja jedzienia frakcji przez miasto
        if (fraction.food > (self.population * 2)):
            self.population = self.population * 1.5  # jedzenie jest
            fraction.food = fraction.food - (self.population * 2)
        elif (fraction.food > (self.population)):
            self.population = self.population * 1.2
            fraction.food = fraction.food - (self.population * 1.2)
        elif (fraction.food < self.population):
            self.population = self.population * 0.7  # głod

    def build(self, fraction, a): #budowa miasta
        super().build(fraction, a)
        self.level += 1
