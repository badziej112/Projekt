from Ground import Ground
from City import City
from Farm import Farm
from Mine import Mine
from Fraction import Fraction
import random

class Mapa:

    def __init__(self, size):
        self.size = size
        self.ground_objects = {}
        self.fraction1 = Fraction("T", 1, 1)
        self.fraction4 = Fraction("W", 1, self.size)
        self.fraction3 = Fraction("A", self.size, self.size)
        self.fraction2 = Fraction("B", self.size, 1)

    def draw(self): #wstępne narysowanie mapy

            """Metoda rysująca mapę stworzoną przez obiekty klasy Ground i zapisanie wartości
                jedzenia i materiału do słownika"""

            for y in range(1, self.size + 1):
                for x in range(1, self.size +1):
                        self.base_object = Ground(x, y)
                        self.base_object.update_object_new()
                        self.ground_objects[x, y] = self.base_object
    def show(self): #pokazanie mapy

        """Pokazanie wyglądu mapy w postaci listy symboli w liście"""

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

        """Metoda aktualizuje słownika ground_objects o nowe wartości."""

        self.base_object = map_object
        self.base_object.update_object()
        self.ground_objects[map_object.x, map_object.y] = self.base_object

    def build_city(self, fraction, x, y, population): #budowanie miasta (nwm jak zbić wszystkie funckcje budujące w 1)

        """Metoda budująca miasto i aktualizuje słownik pola o symbol i wartośc miasta, oraz dodanie symbolu miasta
        słownika aby było widoczne podczas używania mapa.show()"""

        self.base_object = Ground(x, y)
        self.ground_objects[x, y].update_object(self.base_object.build_construction(City(x, y, population), fraction)) #zaktualizowanie słownika danego pola na mapie o symbol i wartość miasta
        self.ground_objects[x, y].symbol = self.ground_objects[x, y].symbol + "C" + fraction.symbol #dodanie symbolu miasta ogólnie (żeby było widać na funkcji mapa.show())

    def build_farm(self, fraction, x, y): #budowanie farm

        """"Metoda budująca farmę i aktualizuje słownik pola o symbol i wartośc miasta, oraz dodanie symbolu miasta
        słownika aby było widoczne podczas używania mapa.show()"""

        self.base_object = Ground(x, y)
        self.ground_objects[x, y].update_object(self.base_object.build_construction(Farm(x, y), fraction))    #zaktualizowanie słownika danego pola na mapie o symbol i wartość farmy
        self.ground_objects[x, y].symbol = self.ground_objects[x, y].symbol + "Fa" + fraction.symbol    #dodanie symbolu farmy ogólnie (żeby było widać na funkcji mapa.show())

    def build_mine(self, fraction, x, y): #budowanie kopalni

        """"Metoda budująca kopalnię i aktualizuje słownik pola o symbol i wartośc miasta, oraz dodanie symbolu miasta
               słownika aby było widoczne podczas używania mapa.show()"""

        self.base_object = Ground(x, y)
        self.ground_objects[x, y].update_object(self.base_object.build_construction(Mine(x, y), fraction))    #zaktualizowanie słownika danego pola na mapie o symbol i wartość kopalni
        self.ground_objects[x, y].symbol = self.ground_objects[x, y].symbol + "Mi" + fraction.symbol    #dodanie symbolu kopalni ogólnie (żeby było widać na funkcji mapa.show())

    def collect_food(self, fraction, x, y): #zbiory jedzenia przez farme

        """"Metoda zbierająca jedzenie dla danej frakcji. Sprawdza czy w słowniku ground_objects nie znajduje
        się wartość mniejsza niż wartość pożądana do zebrania."""

        self.building = Farm(x, y)
        value = self.building.build_job(fraction)
        if self.ground_objects[x, y].base_object['F'] >= value:
            new_value = {"F": self.ground_objects[x, y].base_object['F'] - value}#wartość zebranego surowca
            self.ground_objects[x ,y].base_object.update(new_value)#wyciągnięcie z mapy tej samej ilości surowca

    def collect_resources(self, fraction, x, y): #zbiory materiałów z kopalnie

        """"Metoda zbierająca surowce dla danej frakcji. Sprawdza czy w słowniku ground_objects nie znajduje
                się wartość mniejsza niż wartość pożądana do zebrania."""

        self.building = Mine(x, y)
        value = self.building.build_job(fraction)
        if self.ground_objects[x, y].base_object['M'] >= value:
            new_value = {"M": self.ground_objects[x, y].base_object['M'] - value}#wartość zebranego surowca
            self.ground_objects[x, y].base_object.update(new_value) #wyciągnięcie z mapy tej samej ilości surowca

    def print_object(self, x, y): #pomocnicze drukowanie obiektów na polu

        print(self.ground_objects[x, y].base_object)


    def auto_build(self, x, y, fraction, population): #automatyczne budowanie budynków jeśli to możliwe

        """Metoda budująca budynki dla frakcji: jeśli nie ma miasta - buduje miasto, jeżeli farmy - farmę,
        jeżeli kopalnię - kopalnię. Pozycje na których mają się budować są wybierane losowa z sąsiednich pól."""

        position = []
        pos_x = []
        pos_y = []

        for b in range(y-1, y+2):
            for a in range(x-1, x+2):
                if (a > 0 and b > 0 and a <= self.size and b <= self.size):  # ify żeby nie zbudowało poza mapą
                    position.append((a, b))

        for i in range(position.__len__()):
            for j in range(2):
                if j == 0:
                    pos_x.append(position[i][j])
                if j == 1:
                    pos_y.append(position[i][j])

        position.clear()
        while pos_x.__len__() != 0:
            a = random.randint(0, pos_x.__len__() - 1)
            if (self.ground_objects[pos_x[a], pos_y[a]].symbol == "X" and fraction.material >= 1000):  # najpierw miasta
                self.build_city(fraction, pos_x[a], pos_y[a], population)
            if (self.ground_objects[pos_x[a], pos_y[a]].symbol == "XC" + fraction.symbol and fraction.material >= 500):  # potem kopalnie
                self.build_mine(fraction, pos_x[a], pos_y[a])
            if (self.ground_objects[pos_x[a], pos_y[a]].symbol == "XC" + fraction.symbol + "Mi" + fraction.symbol and fraction.material >= 500):  # na końcu farmy
                self.build_farm(fraction, pos_x[a], pos_y[a])
            if self.ground_objects[pos_x[a], pos_y[a]].symbol.__contains__("C"):
                if (self.ground_objects[pos_x[a], pos_y[a]].symbol[1] == "C" and self.ground_objects[pos_x[a], pos_y[a]].symbol[2] != fraction.symbol):
                    war = random.randint(0, 4)
                    if war == 1:
                        self.base_object = Ground(pos_x[a], pos_y[a])
                        self.base_object.update_object_new()
                        self.ground_objects[pos_x[a], pos_y[a]] = self.base_object
                        self.build_city(fraction, pos_x[a], pos_y[a], population)
            pos_x.remove(pos_x[a])
            pos_y.remove(pos_y[a])

    def check_city(self, fraction): #funkcja sprawdzająca pozycje miast danej frakcji (te funkcje można chyba jakoś zbić w jedną)

        """Funckja sprawdzająca pozycje miast danej frakcji zwracająca je."""

        position = [] #lista tupli pozycji miast
        for x in range(1, self.size + 1): #pętla sprawdzająca położenie miast
            for y in range(1, self.size + 1):
                if(self.ground_objects[x, y].symbol[1:3] == "C" + fraction.symbol):
                    position.append((x,y)) #dodanie do współrzędnych do listy
        return position

    def check_mine(self, fraction): #funkcja sprawdzająca pozycje kopalń danej frakcji (te funkcje można chyba jakoś zbić w jedną)

        """Funckja sprawdzająca pozycje kopalń danej frakcji zwracająca je."""

        position = []   #lista tupli pozycji kopalń
        for x in range(1, self.size + 1):   #pętla sprawdzająca położenie kopalń
            for y in range(1, self.size + 1):
                if(self.ground_objects[x, y].symbol[3:6] == "Mi" + fraction.symbol):
                    position.append((x,y))  #dodanie do współrzędnych do listy
        return position

    def check_farm(self, fraction): #funkcja sprawdzająca pozycje farm danej frakcji (te funkcje można chyba jakoś zbić w jedną)

        """Funckja sprawdzająca pozycje farm danej frakcji zwracająca je."""

        position = []   #lista tupli pozycji farm
        for x in range(1, self.size + 1):   #pętla sprawdzająca położenie farm
            for y in range(1, self.size + 1):
                if (self.ground_objects[x, y].symbol[6:] == "Fa" + fraction.symbol):
                    position.append((x, y)) #dodanie do współrzędnych do listy
        return position

    def show_fraction(self, fraction): #podgląd frakcji

        """Pokazuje dane frakcji. (surowce, materiały, punkty, symbol"""

        print("------------")
        fraction.show_fraction()
        print("------------")

    def consume(self, fraction, x, y, population): #spożycie jedzenie przez ludzi w miastach frakcji

        """Spożywanie jedzenia przez ludzi w miastach."""

        self.city = City(x, y, population)
        if self.city.build_job(fraction) != True:  # jeśli jest jedzenie, punkty frakcji zwiększają się
            self.city.build_job(fraction)
            fraction.points += self.city.population
        else:
            self.city.build_job(fraction)
            fraction.points -= self.city.population * 2  # jeśli nie ma jedzenia zmniejszają
        return self.city.population




