
class Fraction:  # definiuje właściwości całej frakcji

    def __init__(self, symbol, x, y):
        self.symbol = symbol
        self.points = 0
        self.food = 5000
        self.material = 5000
        self.x = x
        self.y = y

    def show_fraction(self): #pokazanie frakcji (pomocnicze)
        print("Symbol: ", self.symbol)
        print("Food: ", self.food)
        print("Materials:", self.material)
        print("Points:", self.points)
