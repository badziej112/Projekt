from AbstractBuilding import AbstractBuilding

class City(AbstractBuilding):

    def __init__(self, x, y, population):
        super().__init__(x, y, "C")
        self.population = population

    def consume(self, fraction): # konsumpcja jedzienia frakcji przez miasto
        if (fraction.food > (self.population * 2)): #przyrost populacji podczas dużej ilości jedzenia
            fraction.food = fraction.food - (self.population * 1.5) #frakcja konsumuje zapasy
            self.population = self.population * 1.5  #rozwój populacji
            return False
        elif (fraction.food >= (self.population)): #normalna ilość jedzenia
            fraction.food = fraction.food - self.population #konsumowanie zapasoów
            self.population = self.population * 1.2 #rozwój populacji
            return False
        elif (fraction.food < self.population): #głód
            self.population = self.population * 0.7  #spadek populacji
            return True

    def build(self, fraction, a): #budowa miasta
        super().build(fraction, a)
