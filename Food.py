import random
from AbstractResource import AbstractResource

class Food(AbstractResource):

    def __init__(self):

        super().__init__("F")
        self.number = random.randint(10, 1500)

    def generate(self): #losowe wygenerowanie liczby jedzenia

        """Wygenerowanie losowej ilości materałów."""

        return {"F": self.number}