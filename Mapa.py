import random
from Ground import Ground

class Map:

    def __init__(self, size):
        self.size = size
        self.objects_on_map = {}

    def add(self, map_object):
        self.base_object = map_object
        self.base_object.update()
        self.objects_on_map[map_object.position] = self.base_object

    def show(self):
        for y in range(1, self.size + 1):
            object_list = []
            i = 0
            for x in range(1, self.size + 1):
                object_list.append(self.objects_on_map[(x, y)].symbol)
                i += 1
                if i == self.size:
                    print(object_list)

        print(self.size * 5 * "-")

    def print_object(self, position):
        print(self.objects_on_map[position].base_object)

    def draw(self):
            for y in range(1, self.size + 1):
                for x in range(1, self.size +1):
                        self.add(Ground((x,y)))


mapa = Map(10)

mapa.draw()

mapa.show()

mapa.print_object((1,2))
mapa.print_object((3,2))







