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
        self.f = 0


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
    return math.ceil(math.sqrt((current.x - goal.x)**2 + (current.y - goal.y)**2))


matrix = convert_matrix(src_matrix)


start = node(1,0)
end = node(10, 4)


def aStar(start, end):
    open_set = [start]
    closed_set = []
    neighboors = []
    f_costs = []
    h_costs = []
    g_costs = []
    finished = False

    while not finished:
        for node in open_set:
            node.h = heuristic(node, end)
            node.f = node.g + node.h
            h_costs.append(node.h)
            f_costs.append(node.f)


        for i, node in enumerate(open_set):
            hej
            

        


        '''current = open_set[f_costs.index(min(f_costs))]
        open_set.remove(current)
        f_costs.remove(current.f)
        g_costs.remove(current.g)
        h_costs.remove(current.h)
        closed_set.append(current)'''

        


        if current == end:
            finished = True


        for neighboor in get_neighboors(current, matrix):
            if neighboor != None:
                neighboor.g += 10
                if (neighboor.wall == True) or (neighboor in closed_set):
                    continue

                if (neighboor.g < current.g) or (neighboor not in open_set):
                    neighboor.h = heuristic(neighboor, end)
                    neighboor.f = neighboor.g + neighboor.h
                    if neighboor not in open_set:
                        open_set.append(neighboor)                
            



            


    '''for open_node in open_set:
        for neighboor in get_neighboors(open_node, matrix):
            if neighboor != None:
                neighboor.g += 10
                neighboor.h += heuristic(neighboor, end)
                neighboor.f = neighboor.g + neighboor.h
                neighboor.parent = open_node
                #open_set.append(neighboor)
        closed_set.append(open_node)
        open_set.remove(open_node)'''



aStar(start, end)

        
