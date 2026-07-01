# https://www.codewars.com/kata/53f1015fa9fe02cbda00111a

import random

class Ghost:
    def __init__(self):
        colors = ['white', 'yellow', 'purple', 'red']
        self.color = random.choice(colors)
