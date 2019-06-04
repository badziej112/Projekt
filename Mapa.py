from Ground import Ground
from Fraction import Fraction

class Mapa:

    def __init__(self, size):
        self.size = size
        self.ground_objects = {}
        self.fraction1 = Fraction("T", 1, 1)
        self.fraction2 = Fraction("W", 10, 10)

    def draw(self): #wstępne narysowanie mapy
            for y in range(1, self.size + 1):
                for x in range(1, self.size +1):
                        self.base_object = Ground(x,y)
                        self.base_object.update_object_new()
                        self.ground_objects[x, y] = self.base_object
    def show(self): #pokazanie mapy
        for y in range(1, self.size + 1):
            area = []
            i = 0
            for x in range(1, self.size + 1):
                area.append(self.ground_objects[x, y].symbol)
                i += 1
                if i == self.size:
                    print(area)

        print(self.size * 5 * " ")

    def add(self, map_object): #dodawanie obiektu do mapy(nwm jak bardzo jest to potrzebne)
        self.base_object = map_object
        self.base_object.update_object()
        self.ground_objects[map_object.x, map_object.y] = self.base_object

    def build_city(self, fraction, x, y): #budowanie miasta (nwm jak zbić wszystkie funckcje budujące w 1)
        self.base_object = Ground(x, y)
        self.ground_objects[x, y].update_object(self.base_object.build_city(fraction, x, y)) #zaktualizowanie słownika danego pola na mapie o symbol i wartość miasta
        self.ground_objects[x, y].symbol = self.ground_objects[x, y].symbol + "C" + fraction.symbol #dodanie symbolu miasta ogólnie (żeby było widać na funkcji mapa.show())

    def build_farm(self, fraction, x, y): #budowanie farm
        self.base_object = Ground(x, y)
        self.ground_objects[x, y].update_object(self.base_object.build_farm(fraction, x, y))    #zaktualizowanie słownika danego pola na mapie o symbol i wartość farmy
        self.ground_objects[x, y].symbol = self.ground_objects[x, y].symbol + "Fa" + fraction.symbol    #dodanie symbolu farmy ogólnie (żeby było widać na funkcji mapa.show())

    def build_mine(self, fraction, x, y): #budowanie kopalni
        self.base_object = Ground(x, y)
        self.ground_objects[x, y].update_object(self.base_object.build_mine(fraction, x, y))    #zaktualizowanie słownika danego pola na mapie o symbol i wartość kopalni
        self.ground_objects[x, y].symbol = self.ground_objects[x, y].symbol + "Mi" + fraction.symbol    #dodanie symbolu kopalni ogólnie (żeby było widać na funkcji mapa.show())

    def harvest(self, fraction, x, y): #zbiory jedzenia przez farme
        self.base_object = Ground(x, y)
        new_value = {"F": self.ground_objects[x, y].base_object['F'] - self.base_object.harvest(fraction, x, y)}#wartość zebranego surowca
        self.ground_objects[x ,y].base_object.update(new_value)#wyciągnięcie z mapy tej samej ilości surowca

    def collect(self, fraction, x, y): #zbiory materiałów z kopalnie
        self.base_object = Ground(x, y)
        new_value = {"M": self.ground_objects[x, y].base_object['M'] - self.base_object.collect(fraction, x, y)}#wartość zebranego surowca
        self.ground_objects[x, y].base_object.update(new_value) #wyciągnięcie z mapy tej samej ilości surowca

    def print_object(self, x, y): #pomocnicze drukowanie obiektów na polu
        print(self.ground_objects[x, y].base_object)

    def check_neighbour(self, x, y):
        if (x < self.size):
            if (self.ground_objects[x, y].symbol == self.ground_objects[x + 1, y]):
                return True
        if (x > 1):
            if (self.ground_objects[x, y].symbol == self.ground_objects[x - 1, y]):
                return True
        if (y < self.size):
            if (self.ground_objects[x, y].symbol == self.ground_objects[x, y + 1]):
                return True
        if (y > 1):
            if (self.ground_objects[x, y].symbol == self.ground_objects[x, y - 1]):
                return True
        else:
            return False

    def auto_build(self, x, y, fraction): #automatyczne budowanie budynków jeśli to możliwe
        for b in range(y-1, y+2):
            for a in range(x-1, x+2):
                if(a > 0 and b > 0 and a <= self.size and b <= self.size): #ify żeby nie zbudowało poza mapą
                    if(self.ground_objects[a, b].symbol == "X" and fraction.material >= 1000): # najpierw miasta
                        self.build_city(fraction, a, b)
                    if (self.ground_objects[a, b].symbol == "XC" + fraction.symbol and fraction.material >= 500): #potem kopalnie
                        self.build_mine(fraction, a, b)
                    if (self.ground_objects[a, b].symbol == "XC" + fraction.symbol + "M" + fraction.symbol  and fraction.material >= 500): #na końcu farmy
                        self.build_farm(fraction, a, b)

    def check_city(self, fraction): #funkcja sprawdzająca pozycje miast danej frakcji (te funkcje można chyba jakoś zbić w jedną)
        position = [] #lista tupli pozycji miast
        for x in range(1, self.size + 1): #pętla sprawdzająca położenie miast
            for y in range(1, self.size + 1):
                if(self.ground_objects[x, y].symbol[1:3] == "C" + fraction.symbol):
                    position.append((x,y)) #dodanie do współrzędnych do listy
        return position

    def check_mine(self, fraction): #funkcja sprawdzająca pozycje kopalń danej frakcji (te funkcje można chyba jakoś zbić w jedną)
        position = []   #lista tupli pozycji kopalń
        for x in range(1, self.size + 1):   #pętla sprawdzająca położenie kopalń
            for y in range(1, self.size + 1):
                if(self.ground_objects[x, y].symbol[3:6] == "Mi" + fraction.symbol):
                    position.append((x,y))  #dodanie do współrzędnych do listy
        return position

    def check_farm(self, fraction): #funkcja sprawdzająca pozycje farm danej frakcji (te funkcje można chyba jakoś zbić w jedną)
        position = []   #lista tupli pozycji farm
        for x in range(1, self.size + 1):   #pętla sprawdzająca położenie farm
            for y in range(1, self.size + 1):
                if (self.ground_objects[x, y].symbol[6:] == "Fa" + fraction.symbol):
                    position.append((x, y)) #dodanie do współrzędnych do listy
        return position

    def show_fraction(self): #podgląd frakcji
        self.fraction1.show_fraction()



