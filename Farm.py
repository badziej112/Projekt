import random
from Event import Event
class Farm:

    def __init__(self, x, y):
        self.symbol = "Fa"
        self.x = x
        self.y = y

    def harvest(self, fraction):
        pogoda = Event()
        pogoda.set_weather()
        a = random.randint(50, 150)
        b = random.randint(0, 15)
        if (pogoda.type > 0):
            fraction.food = (fraction.food + a * pogoda.type)
            return  a
        if (pogoda.type == 0):
            fraction.food = fraction.food + a
            return  a
        if (pogoda.type < 0):
            fraction.food = fraction.food + b
            return  b
        #self.base_object.update("F" = "F" - a)

    def build(self, fraction):
        if (fraction.material > 500):
            fraction.material = fraction.material - 500

    def add_farm(self, fraction):
        return {"Fa"+fraction.symbol: 1}


