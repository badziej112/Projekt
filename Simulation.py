from Mapa import Mapa
import time

class Simulation:

    def __init__(self):

        self.counter = 0

    def start(self):
        while self.counter < 99:
            if self.counter == 0: #czynność startowa
                mapa = Mapa(10) #ustawienie wielkości mapy
                mapa.draw() #narysowanie mapy
                mapa.show() #pokazanie mapy
                time.sleep(0.25)
                mapa.build_city(mapa.fraction1, 1, 1) #budowa początkowa miasta kopalni i farmy
                mapa.build_mine(mapa.fraction1, 1, 1)
                mapa.build_farm(mapa.fraction1, 1, 1)
                mapa.show() #pokazanie mapy po budowie
                time.sleep(0.25)
            position = mapa.check_city(mapa.fraction1) #zebranie współrzędnych miast danej frakcji do 1 zmiennej
            for i in range(position.__len__()): #pętla budująca miasta, farmy i kopalnie
                for j in range(2):
                    if j == 0:
                        x = position[i][j]
                    if j == 1:
                        y = position[i][j]
                mapa.auto_build(x, y, mapa.fraction1) #budowa
            position = mapa.check_mine(mapa.fraction1) #zebranie współrzędnych kopalń danej frakcji do 1 zmiennej
            for i in range(position.__len__()): #pętla zbierająca surowce z każdej kopalni
                for j in range(2):
                    if j == 0:
                        x = position[i][j]
                    if j == 1:
                        y = position[i][j]
                mapa.collect(mapa.fraction1, x, y) #zbiór
            position = mapa.check_farm(mapa.fraction1) #zebranie współrzędnych wszystkich farm danej frakcji do 1 zmiennej
            for i in range(position.__len__()): #pętla zbierająca jedzenie z każdej farmy
                for j in range(2):
                    if j == 0:
                        x = position[i][j]
                    if j == 1:
                        y = position[i][j]
                mapa.harvest(mapa.fraction1, x, y) #zbiór
            mapa.show() #pokazanie mapy po zmianach
            mapa.show_fraction() #wywołanie danych frakcji
            self.counter += 1
            time.sleep(1)

sim = Simulation()
sim.start()
