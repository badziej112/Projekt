from Mapa import Mapa

class Simulation:

    def __init__(self):

        self.counter = 0

    def start(self):

        mapa = Mapa(10) #stworzenie wielkosci mapy

        mapa.draw() #narysowanie mapy

        mapa.show() #świeża mapa

        mapa.print_object(1,1) #obiekty na polu przed budową

        mapa.build_city(mapa.fraction1, 1, 1) #budowanie miasta danej frakcji

        mapa.print_object(1, 1) #obiekty na polu po budowie

        mapa.show() #mapa po zbudowaniu miasta przez frakcje

        mapa.build_farm(mapa.fraction1, 1, 1) #budowanie farmy

        mapa.print_object(1, 1) #obiekty na polu po budowie

        mapa.show() #mapa po zbudowaniu farmy przez frakcje

        mapa.print_object(1, 1) #surowce przed zbiorami

        print(mapa.fraction1.food) #surowce frakcji przed zbiorami

        mapa.harvest(mapa.fraction1, 1, 1) #zbiór

        print(mapa.fraction1.food) #surowce frakcji po zbiorach

        mapa.print_object(1, 1) #surowce po zbiorach

        mapa.build_mine(mapa.fraction1, 1, 1) #zbudowanie kopalni

        mapa.show() #pokazanie mapy po zbudowaniu kopalni

        mapa.build_city(mapa.fraction2, 10, 10) #zbudowanie miasta innej frakcji

        mapa.show()  #pokazanie miasta innej frakcji na mapie


       #mapa.add(Fraction("T", 1, 1))  # tak dodawac frakcje xd

        #mapa.objects_on_map[5, 6].build_city(mapa.objects_on_map[2, 2])  # tak budowac miasta

        #while self.counter < 99:
         #   self.counter = self.counter + 1
            # self.x = random.randint(1, mapa.size)
            # self.y = random.randint(1, mapa.size)
            #mapa.objects_on_map[random.randint(1, mapa.size), random.randint(3, mapa.size)].harvest_food(
             #   mapa.objects_on_map[2, 2])
            #mapa.objects_on_map[random.randint(1, mapa.size), random.randint(3, mapa.size)].harvest_materials(
            #    mapa.objects_on_map[2, 2])

            #mapa.objects_on_map[random.randint(1, mapa.size), random.randint(3, mapa.size)].harvest_food(
            #    mapa.objects_on_map[2, 2])  # expansie
            #mapa.objects_on_map[random.randint(1, mapa.size), random.randint(3, mapa.size)].harvest_materials(
            #    mapa.objects_on_map[2, 2])

            #if (mapa.objects_on_map[self.x, self.y].check_resources() == 0 or mapa.check_neighbour(self.x, self.y)):
            #    mapa.change(self.x, self.y, mapa.objects_on_map[2, 2])
            #if (self.counter % 3):
            #    mapa.show()
            #    mapa.objects_on_map[2, 2].show_fraction()
            #    print("--------------")
            #self.counter = self.counter + 1

sim = Simulation()
sim.start()
