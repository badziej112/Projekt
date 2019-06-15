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

    def build_construction(self, building_class, fraction):    #budowanie

        """Buduje budynek, dodaje jego symbol i wartość do słownika i zwraca ten słownik."""

        self.building = building_class
        self.building.build(fraction) #zbudowanie budynku
        self.building_dict = {}
        self.building = self.building.add_building(fraction)    #dodanie do słownika danych budynku
        return self.building

    def update_object_new(self): #zaktualizowanie słownika na obszarze przy rysowaniu mapy

        """Metoda aktualizująca słownik pola o losowe wartości jedzenia i materiałów."""

        self.base_object.update(self.food_on_map.generate())
        self.base_object.update(self.material_on_map.generate())

    def update_object(self, obj): #aktualizowanie oobszaru na mapie np. przy budowaniu

        """Metoda aktualizująca słownik o zadaną wartość."""

        self.base_object.update(obj)



