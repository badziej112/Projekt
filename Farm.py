import random
from AbstractBuilding import AbstractBuilding
from Event import Event
class Farm(AbstractBuilding):

    def __init__(self, x, y):
        super().__init__(x, y, "Fa")

    def harvest(self, fraction): #zbiór jedzenia w zależności od pogody
        pogoda = Event()
        pogoda.set_weather()
        a = random.randint(50, 150)
        b = random.randint(0, 15)
        if (pogoda.type > 0): #dużo jedzenia bo dobra pogoda
            fraction.food = (fraction.food + a * pogoda.type)
            return  a
        if (pogoda.type == 0): #tak normalnie
            fraction.food = fraction.food + a
            return  a
        if (pogoda.type < 0): #średnia pogoda to mało jedzenia
            fraction.food = fraction.food + b
            return  b

    def build(self, fraction, a): #abstract
        super().build(fraction, a)



