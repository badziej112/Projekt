import random
from AbstractResource import AbstractResource

class Material(AbstractResource):

    def __init__(self):
        super().__init__("M")
        self.number = random.randint(20, 1000)

    def generate(self): #generowanie materiałów
        return {"M": self.number}


