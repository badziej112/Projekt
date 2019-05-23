from Materials import AbstractMaterial

class Food(AbstractMaterial):


    def __init__(self, number):
        super().__init__(number, "F")
        self.object_food = {"F": number}

    def feed(self):
        pass



#food1 = Food(20, "F")