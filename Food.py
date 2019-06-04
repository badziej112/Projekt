import random
from AbstractResource import AbstractResource

class Food(AbstractResource):

    def __init__(self):
        super().__init__("F")
        self.number = random.randint(1000,10000)

    def generate(self): #losowe wygenerowanie liczby jedzenia
        return {"F": self.number}

    def use(self):
        pass
