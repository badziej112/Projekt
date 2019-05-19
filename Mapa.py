from Ground import Ground
from Food import Food

class Map:

    def __init__(self, size):
        self.size = size
        self.objects_on_board = {}

    def add_object_to_map(self, map_object):
        self.objects_on_board[map_object.position] = map_object

    def draw(self):
        for y in range(1, self.size + 1):
            for x in range(1, self.size +1):
                self.add_object_to_map(Ground((x,y)))

    def show(self):
        for y in range(1, self.size + 1):
            object_list = []
            i = 0
            for x in range(1, self.size + 1):
                object_list.append(self.objects_on_board[(x, y)].symbol)
                i += 1
                if i == self.size:
                    print(object_list)

        print(self.size * 5 * "-")

ground = Ground(10)
print(ground.position)

map = Map(10)

map.draw()

map.show()

food1 = Food(20, "Jedzienie" , (1,2), 'F' )

map.add_object_to_map(food1)

map.show()


