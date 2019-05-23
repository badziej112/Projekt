from Food import Food
from Material import Material

class Object():

    def __init__(self, objekt1, objekt2, position):
        self.position = position
        self.base_object = {}
        self.symbol = "X"
        self.base_object.update(objekt1)
        self.base_object.update(objekt2)




food1 = Food(20)
material1 = Material(200)

print(food1.object_food)
print(material1.object_material)

objekt = Object(food1.object_food, material1.object_material, (2,1))

print(objekt.base_object)