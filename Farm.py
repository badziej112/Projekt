import random
from AbstractBuilding import AbstractBuilding
from Event import Event

class Farm(AbstractBuilding):

    def __init__(self, x, y):

        super().__init__(x, y, "Fa")

    def build_job(self, fraction): #zbiór jedzenia w zależności od pogody

        """Metoda wykonująca pracę budynku. Pobiera z pola różną wartość jedzenia w zależności od pogody,."""

        pogoda = Event()
        pogoda.set_weather()#ustawienie pogody
        a = random.randint(50, 100) #losowa wartość przy dobrym zbiorze
        b = random.randint(5, 50) #losowa wartość przy słabym zbiorze
        if (pogoda.type > 0): #dużo jedzenia bo dobra pogoda
            fraction.food = (fraction.food + a * pogoda.type)
            return  a * pogoda.type
        if (pogoda.type == 0): #standardowo
            fraction.food = fraction.food + a
            return  a
        if (pogoda.type < 0): #zła pogoda to mało jedzenia
            fraction.food = fraction.food + b
            return  b

    def build(self, fraction): #abstract

        """Buduje farmę odejmuje jego koszt od zasobów frakcji oraz dodaje punkty rozwoju."""

        if (fraction.material > 500):
            fraction.material = fraction.material - 500
            fraction.points += 50



