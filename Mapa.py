import random
from Ground import Ground
from Object import Object
from Food import Food
from Material import Material

class Map:

    def __init__(self, size):
        self.size = size
        self.objects_on_map = {}

    def add(self, map_object):
        self.objects_on_map[map_object.position] = map_object

    def draw(self):
        for y in range(1, self.size + 1):
            for x in range(1, self.size +1):
                self.add(Ground((x,y)))

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

    def generate(self, map_object1, n):
        while(n != 100):
            c = random.randint(1, 10)
            d = random.randint(1, 10)
            if self.objects_on_map[(c,d)].symbol == 'G':
                self.objects_on_map[(c,d)] = map_object1
            return mapa.generate(map_object1, n+1)

#a = random.randint(1,10)
#b = random.randint(1,10)
ground = Ground((1,1))

mapa = Map(10)

mapa.draw()

mapa.show()

#food1 = Food(random.randint(50,100))
#material1 = Material(random.randint(10,1000))

#objekt = Object(food1.object_food, material1.object_material, (a,b))

#mapa.add(objekt)

#mapa.show()

a = random.randint(1,10)
b = random.randint(1,10)

food1 = Food(random.randint(10,200))
material1 = Material(random.randint(1,1000))

objekt1 = Object(food1.object_food, material1.object_material, (a,b))

mapa.generate(objekt1,  1)


mapa.show()





