import random

class Dice:

    def __init__(self, sides=6):
        self.sides = sides
    
    def roll(self):
        return random.choice(self.sides)