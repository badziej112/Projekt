import random
from AbstractResource import AbstractResource

class Material(AbstractResource):

    def __init__(self):
        super().__init__("M")
        self.number = random.randint(10,100)

    def generate(self):
        return {"M": self.number}

    def use(self):
        pass


