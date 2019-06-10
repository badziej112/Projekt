import random
class Event:

    def __init__(self):
        self.type = 0

    def set_weather(self): #ustawienie typu pogody
        self.type = random.randint(-2, 3)