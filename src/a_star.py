import math
from graph import src_matrix


class Node():
    def __init__(self, pos=None, wall=False, parent=None):
        self.pos = pos
        self.x = self.pos[0]
        self.y = self.pos[1]
        self.wall = wall
        self.parent = parent
        self.g = 0
        self.h = 0
        self.f = self.g + self.h

    '''def get_neighboors(self):
        if self.pos != None:
            x, y = self.x, self.y
            
            # Check if node is a corner
            if self.pos == (0, 0): 
                up, left = None, None
                down, right = matrix[y+1][x], matrix[y][x+1]
            elif self.pos == (0, self.y_max): 
                left, down = None, None
                right, up = matrix[y][x+1], matrix[y-1][x]
            elif self.pos == (self.x_max, 0): 
                up, right = None, None
                down, left = matrix[y+1][x], matrix[y][x-1]
            elif self.pos == (self.x_max, self.y_max): 
                down, right = None, None
                up, left = matrix[y-1][x], matrix[y][x-1]
            
            # Check if node is an edge
            elif ((x > 0) and (x < self.x_max)) and (y == self.y_max): 
                down = None
                up, left, right = matrix[y-1][x], matrix[y][x-1], matrix[y][x+1]
            elif ((x > 0) and (x < self.x_max)) and (y == 0): 
                up = None
                down, left, right = matrix[y+1][x], matrix[y][x-1], matrix[y][x+1]
            elif ((y > 0) and (y < self.y_max)) and (x == self.x_max): 
                right = None
            elif ((y > 0) and (y < self.y_max)) and (x == 0): 
                left = None

            else:
                up = matrix[y-1][x]      # (x, y-1)
                down = matrix[y+1][x]    # (x, y+1)
                left = matrix[y][x-1]    # (x-1, y)
                right = matrix[y][x+1]   # (x+1, y)

            return [up, down, left, right]
        else:
            return None'''


def get_neighboors(node, graph):
    x, y = node.pos
    x_max, y_max = len(graph[0])-1, len(graph)-1
    up, down, left, right = None, None, None, None

    if x == 0:
        if y == 0:
            down = graph[y+1][x]
            right = graph[y][x+1]
        elif y == y_max:
            up = graph[y-1][x]
            right = graph[y][x+1]
        else:
            down = graph[y+1][x]
            left = graph[y][x-1]
            right = graph[y][x+1]
    elif x == x_max:
        if y == 0:
            down = graph[y+1][x]
            left = graph[y][x-1]
        elif y == y_max:
            left = graph[y][x-1]
            up = graph[y-1][x]
    elif (y == 0) and (x > 0) and (x < x_max):
        down = graph[y+1][x]
        left = graph[y][x-1]
        right = graph[y][x+1]
    elif (y == y_max) and (x > 0) and (x < x_max):
        left = graph[y][x-1]
        right = graph[y][x+1]
        up = graph[y-1][x]
    else:
        up = graph[y-1][x]      # (x, y-1)
        down = graph[y+1][x]    # (x, y+1)
        left = graph[y][x-1]    # (x-1, y)
        right = graph[y][x+1]   # (x+1, y)

    return [up, down, left, right]


def convert_matrix(matrix):
    for i, y in enumerate(matrix):
        for j, x in enumerate(y):
            if matrix[i][j] == 1:
                matrix[i][j] = Node((j, i), True)
            else:
                matrix[i][j] = Node((j, i), False)
    return matrix


def node(x, y): 
    return matrix[y][x]


def heuristic(current, goal):
    return math.ceil(math.sqrt((current[0] - goal[0])**2 + (current[1] - goal[1])**2))


matrix = convert_matrix(src_matrix)


start = node(1,0)
end = node(16, 23)


def aStar(start, end):
    open = [start]
    closed = []
    finished = False
    print(get_neighboors(start, matrix))


aStar(start, end)

        
