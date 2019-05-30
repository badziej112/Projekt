from Fraction import Fraction

class City:

    def __init__(self, x, y):
        self.symbol = "C"
        self.x = x
        self.y = y
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

    def build(self, fraction): #budowa miasta
        if (fraction.material > 1000):
            self.level = self.level + 1
            fraction.material = fraction.material - 1000

    def add_city(self, fraction): #dodanie symbolu do mapy
        return {"C"+fraction.symbol: 1}
