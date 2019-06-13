from Food import Food
from Material import Material

class Ground():

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.base_object = {}
        self.food_on_map = Food()
        self.material_on_map = Material()
        self.symbol = "X"

    def update_object_new(self): #zaktualizowanie słownika na obszarze przy rysowaniu mapy
        self.base_object.update(self.food_on_map.generate())
        self.base_object.update(self.material_on_map.generate())

    def update_object(self, obj): #aktualizowanie oobszaru na mapie np. przy budowaniu
        self.base_object.update(obj)

    def build(self, building_class, cost, fraction):    #budowanie
        self.building = building_class
        self.building.build(fraction, cost) #zbudowanie budynku
        self.building_dict = {}
        self.building = self.building.add_building(fraction)    #dodanie do słownika danych budynku
        fraction.points += 50   #zwiększenie liczby punktów rozwoju frakcji za budowę
        return self.building

