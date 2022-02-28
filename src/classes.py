import math

class Node():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    

    def H(self):
        return math.sqrt(self.x^2 + self.y^2)