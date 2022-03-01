import math

class Node():
    def __init__(self, pos=None, parent=None,):
        self.pos = pos
        self.parent = parent
        self.h = H(self.pos)
        self.g = 0
        self.f = self.g + self.h
        self.wall = True

    def H(self): return math.sqrt(self.pos[0]^2 + self.pos[1]^2)
    
    def get_position(self): return self.pos
    
    def get_parent(self): return self.parent

    def get_neighboors(self):
        return [
                (self.pos[0]+1, self.pos[1]), 
                (self.pos[0]-1, self.pos[1]),
                (self.pos[0], self.pos[1]+1),
                (self.pos[0], self.pos[1]-1)
                ]

board = [
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0]
        ]

start = (0, 0)
phejejejks
end = (6, 6)



def H():
    return math.sqrt(self.x^2 + self.y^2)

def aStar(start, end):
    open = {start}
    closed = {}
    g = {}
    parents = {}
    g[start] = 0
    parents[start] = start
