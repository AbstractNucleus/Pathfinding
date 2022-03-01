import math

class Node():
    def __init__(self, pos=None, matrix=None):
        self.pos = pos
        self.matrix = matrix
        self.x = self.pos[0]
        self.y = self.pos[1]
        self.x_max = len(matrix[0])-1
        self.y_max = len(matrix)-1
    
    def get_position(self): 
        return (self.x, self.y)

    def is_walkable(self):
        if self.matrix[self.y][self.x] == 0: return True
        else: return False

    def get_neighboors(self):
        if self.pos != None:
            x, y = self.x, self.y
            up = (x, y-1)
            down = (x, y+1)
            left = (x-1, y)
            right = (x+1, y)
            
            if self.pos == (0, 0): up, left = None, None
            elif self.pos == (0, self.y_max): left, down = None, None
            elif self.pos == (self.x_max, 0): up, right = None, None
            elif self.pos == (self.x_max, self.y_max): down, right = None, None

            elif ((x > 0) and (x < self.x_max)) and (y == self.y_max): down = None
            elif ((x > 0) and (x < self.x_max)) and (y == 0): up = None
            elif ((y > 0) and (y < self.y_max)) and (x == self.x_max): right = None
            elif ((y > 0) and (y < self.y_max)) and (x == 0): left = None

            return [up, down, left, right]
        else:
            return None


matrix = [
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0]
        ]

def heuristic(source, dest):
    dxy = dest - source
    return math.sqrt(dxy[0]^2 + dxy[1]^2)




start = (0, 0)
end = (6, 6)



def aStar(start, end):
    open = {start}

