from Materials import AbstractMaterial

class Food(AbstractMaterial):


    def __init__(self, number, typename, position,symbol):
        super().__init__(number, typename,position,symbol)

    def feed(self):
        pass

