from Materials import AbstractMaterial

class Material(AbstractMaterial):

    def __init__(self, number):
        super().__init__(number, "Ma")
        self.object_material = {"M": number}

    def use(self):
        pass

#material1 = Material(200, "M")