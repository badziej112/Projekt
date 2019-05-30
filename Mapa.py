from Ground import Ground
from Fraction import Fraction

class Mapa:

    def __init__(self, size):
        self.size = size
        self.ground_objects = {}
        self.fraction1 = Fraction("T", 1, 1)

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

    def add(self, map_object): #dodawanie obiektu do mapy
        self.base_object = map_object
        self.base_object.update_object()
        self.ground_objects[map_object.x, map_object.y] = self.base_object

    def build_city(self, fraction, x, y): #budowanie miasta
        self.base_object = Ground(x, y)
        self.ground_objects[x, y].update_object(self.base_object.build_city(fraction, x, y))
        self.ground_objects[x, y].symbol = self.ground_objects[x, y].symbol + "C" + fraction.symbol

    def build_farm(self, fraction, x, y): #budowanie farm
        self.base_object = Ground(x, y)
        self.ground_objects[x, y].update_object(self.base_object.build_farm(fraction, x, y))
        self.ground_objects[x, y].symbol = self.ground_objects[x, y].symbol + "Fa" + fraction.symbol

    def harvest(self, fraction, x, y): #zbiory jedzenia przez farme
        self.base_object = Ground(x, y)
        new_value = {"F": self.ground_objects[x,y].base_object['F'] - self.base_object.harvest(fraction, x, y)}
        self.ground_objects[x ,y].base_object.update(new_value)

    def print_object(self, x, y): #pomocnicze drukowanie obiektów na polu
        print(self.ground_objects[x, y].base_object)

    def change(self, x, y, map_object):  #######pomocnicza zmiana obiektów
        self.base_object = map_object
        self.ground_objects[x, y] = self.base_object

    def check_neighbour(self, x, y):
        if (x < self.size):
            if (self.objects_on_map[x, y].symbol == self.objects_on_map[x + 1, y]):
                return True
        if (x > 1):
            if (self.objects_on_map[x, y].symbol == self.objects_on_map[x - 1, y]):
                return True
        if (y < self.size):
            if (self.objects_on_map[x, y].symbol == self.objects_on_map[x, y + 1]):
                return True
        if (y > 1):
            if (self.objects_on_map[x, y].symbol == self.objects_on_map[x, y - 1]):
                return True
        else:
            return False


#mapa = Mapa(10)

#mapa.draw()

#mapa.show()

#mapa.print_object(2,2)



