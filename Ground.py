from Food import Food
from Material import Material

class Ground():

    def __init__(self, position):
        self.position = position
        self.base_object = {}
        self.base_object1 = Food()
        self.base_object2 = Material()
        self.symbol = "X"

    def update(self):
        self.base_object.update(self.base_object1.generate())
        self.base_object.update(self.base_object2.generate())



