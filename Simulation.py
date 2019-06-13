from Mapa import Mapa
import csv
import random
import time

class Simulation:

    def __init__(self, size, req_points):

        self.counter = 0
        self.mapa = Mapa(size)  # ustawienie wielkości mapy
        self.req_points = req_points
        self.city_population = {}

    @staticmethod
    def scan_map(fraction, mapa):

        #funkcja sprawdzająca czy cała mapa nie jest zajęta przez 1 frakcję

        a = []
        for y in range(1, mapa.size + 1): #dodaje do listy liczbę 1 gdy jest na mapie budynek danej frakcji
            for x in range(1, mapa.size + 1):
                if mapa.ground_objects[x, y].symbol.__contains__(fraction.symbol):
                    a.append(1)
                else:
                    a.append(0)

        b = []
        for i in range(a.__len__()): #lista przypadku gdy cała mapa byłaby zajęta przez frakcję
            b.append(1)

        if a == b: #przyrównanie list
            print("Wygrała frakcja {}{}!".format("z symbolem: ", fraction.symbol))
            exit() #koniec

    @classmethod
    def check_win(cls, a, b ,c ,d, mapa):

        #sprawdzenie czy frakcja nie przekroczyła punktów rozwoju

        cls.req_points = 80000 #wymagane punkty rozwoju do wygrania

        if a != None: #sprawdzenie czy frakcja istnieje, potem sprawdza zwycięstwo
            cls.scan_map(b, mapa)
            if a.points >= cls.req_points:
                name = a.symbol
                print("Wygrała frakcja {}{}!".format("z symbolem: ", name))
                exit()

        if b != None:
            cls.scan_map(b, mapa)
            if b.points >= cls.req_points:
                name = b.symbol
                print("Wygrała frakcja {}{}!".format("z symbolem: ", name))
                exit()

        if c != None:
            cls.scan_map(b, mapa)
            if c.points >= cls.req_points:
                name = c.symbol
                print("Wygrała frakcja {}{}!".format("z symbolem: ", name))
                exit()

        if d != None:
            cls.scan_map(b, mapa)
            if d.points >= cls.req_points:
                name = d.symbol
                print("Wygrała frakcja {}{}!".format("z symbolem: ", name))
                exit()

    @staticmethod
    def check_pos(a, object):

        #Metoda sprawdzająca pozycje wszystkich miast danej frakcji

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

        #Metoda sprawdzająca pozycje wszystkich kopalni danej frakcji

        position = object.check_mine(a)
        for i in range(position.__len__()):  # pętla zbierająca surowce z każdej kopalni
            for j in range(2):
                if j == 0:
                    x = position[i][j]
                if j == 1:
                    y = position[i][j]
            object.collect_resources(a, x, y)

    @staticmethod
    def check_farm(a, object):

        # Metoda sprawdzająca pozycje wszystkich farm danej frakcji

        position = object.check_farm(a)  # zebranie współrzędnych wszystkich farm danej frakcji do 1 zmiennej
        for i in range(position.__len__()):  # pętla zbierająca jedzenie z każdej farmy
            for j in range(2):
                if j == 0:
                    x = position[i][j]
                if j == 1:
                    y = position[i][j]
            object.collect_food(a, x, y)  # zbiór

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

            x, y = Simulation.check_pos(self.mapa.fraction1, self.mapa) #wywołanie funkcji zwracającej współrzędne

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
                y.remove(y[a])

            x, y = Simulation.check_pos(self.mapa.fraction2, self.mapa) #wywołanie funkcji zwracającej współrzędne

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
                y.remove(y[a])

            x, y = Simulation.check_pos(self.mapa.fraction3, self.mapa)  # wywołanie funkcji zwracającej współrzędne

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
                y.remove(y[a])

            x, y = Simulation.check_pos(self.mapa.fraction4, self.mapa)  # wywołanie funkcji zwracającej współrzędne

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
                y.remove(y[a])


            Simulation.check_mine(self.mapa.fraction1, self.mapa) #zbiory materiałów 1 frakcji
            Simulation.check_mine(self.mapa.fraction2, self.mapa) #zbiory materiałów 2 frakcji
            Simulation.check_mine(self.mapa.fraction3, self.mapa)  # zbiory materiałów 3 frakcji
            Simulation.check_mine(self.mapa.fraction4, self.mapa)  # zbiory materiałów 4 frakcji
            Simulation.check_farm(self.mapa.fraction1, self.mapa) #zbiory jedzenia 1 frakcji
            Simulation.check_farm(self.mapa.fraction2, self.mapa) #zbiory jedzienia 2 frakcji
            Simulation.check_farm(self.mapa.fraction3, self.mapa)  # zbiory jedzenia 3 frakcji
            Simulation.check_farm(self.mapa.fraction4, self.mapa)  # zbiory jedzienia 4 frakcji

            self.mapa.show_fraction(self.mapa.fraction1) #pokazanie danych frakcji
            self.mapa.show_fraction(self.mapa.fraction2)
            self.mapa.show_fraction(self.mapa.fraction3)
            self.mapa.show_fraction(self.mapa.fraction4)

            self.mapa.show() #pokazanie mapy po zmianach
            if Simulation.check_win(self.mapa.fraction1, self.mapa.fraction2, self.mapa.fraction3, self.mapa.fraction4, self.mapa) == str: #sprawdzenie zwycięstwa na końcu pętli
                win = Simulation.check_win(self.mapa.fraction1, self.mapa.fraction2, self.mapa.fraction3, self.mapa.fraction4)
                print(win)

            with open("sim_save.txt", mode='w') as  save_file: #zapisz do pliku wszystkich danych potrzebnych do odtworzenia symulacji
                save_simulation = csv.writer(save_file, delimiter=',', quotechar='"', quoting = csv.QUOTE_MINIMAL)

                save_simulation.writerow([
                    self.counter,
                    self.req_points,
                    self.mapa.fraction1.symbol, self.mapa.fraction1.points, self.mapa.fraction1.food, self.mapa.fraction1.material, self.mapa.fraction1.x, self.mapa.fraction1.y,
                    self.mapa.fraction2.symbol, self.mapa.fraction2.points, self.mapa.fraction2.food, self.mapa.fraction2.material, self.mapa.fraction2.x, self.mapa.fraction2.y,
                    self.mapa.fraction3.symbol, self.mapa.fraction3.points, self.mapa.fraction3.food, self.mapa.fraction3.material, self.mapa.fraction3.x, self.mapa.fraction3.y,
                    self.mapa.fraction4.symbol, self.mapa.fraction4.points, self.mapa.fraction4.food, self.mapa.fraction4.material, self.mapa.fraction4.x, self.mapa.fraction4.y,
                    self.city_population
                 ])

                for y in range(1, self.mapa.size + 1):
                    for x in range(1, self.mapa.size + 1):
                        save_simulation.writerow([self.mapa.ground_objects[x, y].symbol, self.mapa.ground_objects[x, y].base_object])


            time.sleep(0.25)
            self.counter += 1

        print("REMIS!") #Wyświetla remis jeżeli żadna frakcja nie wygrała po wszystkich cyklach
        exit()

