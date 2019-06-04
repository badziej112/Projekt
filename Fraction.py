
class Fraction:  # definiuje właściwości całej frakcji

    def __init__(self, symbol, x, y):
        self.symbol = symbol
        self.points = 1
        self.multipler = 1.2
        self.food = 100
        self.material = 5000
        self.x = x
        self.y = y

    def progress(self):
        self.points = self.points * self.multipler

    def change_multipler(self, change):
        self.multipler = +change

    def show_fraction(self): #pokazanie frakcji (pomocnicze)
        print("Symbol: ", self.symbol)
        print("Food: ", self.food)
        print("Materials:", self.material)
