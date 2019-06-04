from Food import Food
from Material import Material
from City import City
from Farm import Farm
from Mine import Mine

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

    def build_city(self, fraction, x, y): #budowanie miasta
        self.city = City(x, y)
        self.city.build(fraction, 1000) #zbudowanie miasta
        self.fraction = fraction #przypisanie frakcji (jeszcze nie wiem czy tak trzeba)
        self.building = {} #pusty słownik żeby dodać wartości
        self.building = self.city.add_building(fraction) #dodanie do słownika miasta i jego wartości
        return self.building

    def build_farm(self, fraction, x, y): #budowanie farmy (komentarze analogiczne jak w build_city())
        self.farm = Farm(x, y)
        self.farm.build(fraction, 500)
        self.fraction = fraction
        self.building = {}
        self.building = self.farm.add_building(fraction)
        return self.building

    def build_mine(self, fraction, x, y): #budowanie kopalni (komentarze analogiczne jak w build_city()
        self.mine = Mine(x, y)
        self.mine.build(fraction, 500)
        self.fraction = fraction
        self.building = {}
        self.building = self.mine.add_building(fraction)
        return self.building

    def harvest(self, fraction, x, y): #zbiory jedzenia
        self.farm = Farm(x, y)
        self.fraction = fraction #jesczze nwm czy potrzebne
        return self.farm.harvest(fraction)

    def collect(self, fraction, x, y): #zbiory materiałów
        self.mine = Mine(x, y)
        self.fraction = fraction #jeszce nwm czy potrzebne
        return  self.mine.collect(fraction)



