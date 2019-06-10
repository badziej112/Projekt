from Mapa import Mapa
import random
import time

class Simulation:

    def __init__(self):

        self.counter = 0
        self.mapa = Mapa(15)  # ustawienie wielkości mapy
        self.city_population = {}

    def scan_map(self, fraction): #funkcja sprawdzająca czy cała mapa nie jest zajęta przez 1 frakcję
        a = []
        for y in range(1, self.mapa.size + 1): #dodaje do listy liczbę 1 gdy jest na mapie budynek danej frakcji
            for x in range(1, self.mapa.size + 1):
                if self.mapa.ground_objects[x, y].symbol.__contains__(fraction.symbol):
                    a.append(1)
                else:
                    a.append(0)

        b = []
        for i in range(a.__len__()): #lista przypadku gdy cała mapa byłaby zajęta przez frakcję
            b.append(1)

        if a == b: #przyrównanie list
            print("Wygrała frakcja {}{}!".format("z symbolem: ", fraction.symbol))
            exit() #koniec

    @staticmethod
    def check_win(a, b ,c ,d): #sprawdzenie czy frakcja nie przekroczyła punktów rozwoju
        req_points = 80000 #wymagane punkty rozwoju do wygrania

        if a != None: #sprawdzenie czy frakcja istnieje, potem sprawdza zwycięstwo
            sim.scan_map(a)
            if a.points >= req_points:
                name = a.symbol
                print("Wygrała frakcja {}{}!".format("z symbolem: ", name))
                exit()

        if b != None:
            sim.scan_map(b)
            if b.points >= req_points:
                name = b.symbol
                print("Wygrała frakcja {}{}!".format("z symbolem: ", name))
                exit()

        if c != None:
            sim.scan_map(c)
            if c.points >= req_points:
                name = c.symbol
                print("Wygrała frakcja {}{}!".format("z symbolem: ", name))
                exit()

        if d != None:
            sim.scan_map(d)
            if d.points >= req_points:
                name = d.symbol
                print("Wygrała frakcja {}{}!".format("z symbolem: ", name))
                exit()

    @staticmethod
    def check_pos(a, object):
        position = object.check_city(a)  # zebranie współrzędnych miast danej frakcji do 1 zmiennej
        x = []  # puste listy do ktorych będą wrzucane współrzędne
        y = []
        for i in range(position.__len__()):  # pętla budująca miasta, farmy i kopalnie
            for j in range(2):
                if j == 0:
                    x.append(position[i][j])  # dodanie współrzędnych do listy
                if j == 1:
                    y.append(position[i][j])
        return x, y #zwrócenie współrzędnych

    @staticmethod
    def check_mine(a, object):
        position = object.check_mine(a)
        for i in range(position.__len__()):  # pętla zbierająca surowce z każdej kopalni
            for j in range(2):
                if j == 0:
                    x = position[i][j]
                if j == 1:
                    y = position[i][j]
            object.collect(a, x, y)

    @staticmethod
    def check_farm(a, object):
        position = object.check_farm(a)  # zebranie współrzędnych wszystkich farm danej frakcji do 1 zmiennej
        for i in range(position.__len__()):  # pętla zbierająca jedzenie z każdej farmy
            for j in range(2):
                if j == 0:
                    x = position[i][j]
                if j == 1:
                    y = position[i][j]
            object.harvest(a, x, y)  # zbiór

    def start(self):
        while self.counter < 99:
            if self.counter == 0: #czynność startowa
                self.mapa.draw() #narysowanie mapy
                self.mapa.show() #pokazanie mapy
                time.sleep(0.25)
                self.mapa.build_city(self.mapa.fraction1, self.mapa.fraction1.x, self.mapa.fraction1.y, None) #budowa początkowa miasta kopalni i farmy
                self.mapa.build_mine(self.mapa.fraction1, self.mapa.fraction1.x, self.mapa.fraction1.y)
                self.mapa.build_farm(self.mapa.fraction1, self.mapa.fraction1.x, self.mapa.fraction1.y)
                self.mapa.build_city(self.mapa.fraction2, self.mapa.fraction2.x, self.mapa.fraction2.y, None)
                self.mapa.build_mine(self.mapa.fraction2, self.mapa.fraction2.x, self.mapa.fraction2.y)
                self.mapa.build_farm(self.mapa.fraction2, self.mapa.fraction2.x, self.mapa.fraction2.y)
                self.mapa.build_city(self.mapa.fraction3, self.mapa.fraction3.x, self.mapa.fraction3.y, None)  # budowa początkowa miasta kopalni i farmy
                self.mapa.build_mine(self.mapa.fraction3, self.mapa.fraction3.x, self.mapa.fraction3.y)
                self.mapa.build_farm(self.mapa.fraction3, self.mapa.fraction3.x, self.mapa.fraction3.y)
                self.mapa.build_city(self.mapa.fraction4, self.mapa.fraction4.x, self.mapa.fraction4.y, None)  # budowa początkowa miasta kopalni i farmy
                self.mapa.build_mine(self.mapa.fraction4, self.mapa.fraction4.x, self.mapa.fraction4.y)
                self.mapa.build_farm(self.mapa.fraction4, self.mapa.fraction4.x, self.mapa.fraction4.y)
                self.mapa.show() #pokazanie mapy po budowie
                time.sleep(0.25)

            x, y = sim.check_pos(self.mapa.fraction1, self.mapa) #wywołanie funkcji zwracającej współrzędne

            while x.__len__() != 0:
                a = random.randint(0, x.__len__()-1) #wylosowanie z listy losowych współrzędnych
                if self.city_population.__contains__((x[a], y[a])) == False:
                    p = self.mapa.consume(self.mapa.fraction1, x[a], y[a], 10)
                    self.city_population.update({(x[a], y[a]): p})
                elif self.city_population.__contains__((x[a], y[a])) == True:
                    p = self.mapa.consume(self.mapa.fraction1, x[a], y[a], self.city_population[(x[a], y[a])])
                    self.city_population.update({(x[a], y[a]): p})
                self.mapa.auto_build(x[a], y[a], self.mapa.fraction1, None) #losowe tworzenie budynków
                x.remove(x[a])

            x, y = sim.check_pos(self.mapa.fraction2, self.mapa) #wywołanie funkcji zwracającej współrzędne

            while (x.__len__() != 0):
                a = random.randint(0, x.__len__() - 1)  # wylosowanie z listy losowych współrzędnych
                if self.city_population.__contains__((x[a], y[a])) == False:
                    p = self.mapa.consume(self.mapa.fraction2, x[a], y[a], 10)
                    self.city_population.update({(x[a], y[a]): p})
                elif self.city_population.__contains__((x[a], y[a])) == True:
                    p = self.mapa.consume(self.mapa.fraction2, x[a], y[a], self.city_population[(x[a], y[a])])
                    self.city_population.update({(x[a], y[a]): p})
                self.mapa.auto_build(x[a], y[a], self.mapa.fraction2, None)  # losowe tworzenie budynków
                x.remove(x[a])

            x, y = sim.check_pos(self.mapa.fraction3, self.mapa)  # wywołanie funkcji zwracającej współrzędne

            while (x.__len__() != 0):
                a = random.randint(0, x.__len__() - 1)  # wylosowanie z listy losowych współrzędnych
                if self.city_population.__contains__((x[a], y[a])) == False:
                    p = self.mapa.consume(self.mapa.fraction3, x[a], y[a], 10)
                    self.city_population.update({(x[a], y[a]): p})
                elif self.city_population.__contains__((x[a], y[a])) == True:
                    p = self.mapa.consume(self.mapa.fraction3, x[a], y[a], self.city_population[(x[a], y[a])])
                    self.city_population.update({(x[a], y[a]): p})
                self.mapa.auto_build(x[a], y[a], self.mapa.fraction3, None)  # losowe tworzenie budynków
                x.remove(x[a])

            x, y = sim.check_pos(self.mapa.fraction4, self.mapa)  # wywołanie funkcji zwracającej współrzędne

            while (x.__len__() != 0):
                a = random.randint(0, x.__len__() - 1)  # wylosowanie z listy losowych współrzędnych
                if self.city_population.__contains__((x[a], y[a])) == False:
                    p = self.mapa.consume(self.mapa.fraction4, x[a], y[a], 10)
                    self.city_population.update({(x[a], y[a]): p})
                elif self.city_population.__contains__((x[a], y[a])) == True:
                    p = self.mapa.consume(self.mapa.fraction4, x[a], y[a], self.city_population[(x[a], y[a])])
                    self.city_population.update({(x[a], y[a]): p})
                self.mapa.auto_build(x[a], y[a], self.mapa.fraction4, None)  # losowe tworzenie budynków
                x.remove(x[a])


            sim.check_mine(self.mapa.fraction1, self.mapa) #zbiory materiałów 1 frakcji
            sim.check_mine(self.mapa.fraction2, self.mapa) #zbiory materiałów 2 frakcji
            sim.check_mine(self.mapa.fraction3, self.mapa)  # zbiory materiałów 3 frakcji
            sim.check_mine(self.mapa.fraction4, self.mapa)  # zbiory materiałów 4 frakcji
            sim.check_farm(self.mapa.fraction1, self.mapa) #zbiory jedzenia 1 frakcji
            sim.check_farm(self.mapa.fraction2, self.mapa) #zbiory jedzienia 2 frakcji
            sim.check_farm(self.mapa.fraction3, self.mapa)  # zbiory jedzenia 3 frakcji
            sim.check_farm(self.mapa.fraction4, self.mapa)  # zbiory jedzienia 4 frakcji

            self.mapa.show_fraction(self.mapa.fraction1) #pokazanie danych frakcji
            self.mapa.show_fraction(self.mapa.fraction2)
            self.mapa.show_fraction(self.mapa.fraction3)
            self.mapa.show_fraction(self.mapa.fraction4)

            self.mapa.show() #pokazanie mapy po zmianach
            if sim.check_win(self.mapa.fraction1, self.mapa.fraction2, self.mapa.fraction3, self.mapa.fraction4) == str: #sprawdzenie zwycięstwa na końcu pętli
                win = sim.check_win(self.mapa.fraction1, self.mapa.fraction2, self.mapa.fraction3, self.mapa.fraction4)
                print(win)
            time.sleep(0.25)
            self.counter += 1



sim = Simulation()
sim.start()
