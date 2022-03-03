from copy import deepcopy
from math import ceil, sqrt
import json


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


def getNeighboors(node, graph):
    x, y = node.pos

    up = graph[y-1][x]              # (x, y-1)
    down = graph[y+1][x]            # (x, y+1)
    left = graph[y][x-1]            # (x-1, y)
    right = graph[y][x+1]           # (x+1, y)
    up_left = graph[y-1][x-1]       # (x-1, y-1)
    down_right = graph[y+1][x+1]    # (x+1, y+1)
    down_left = graph[y+1][x-1]     # (x-1, y+1)
    up_right = graph[y-1][x+1]      # (x+1, y-1)

    return [up, down, left, right, up_left, up_right, down_left, down_right]


def convertMatrix(matrix):
    for i, y in enumerate(matrix):
        for j, x in enumerate(y):
            if matrix[i][j] == 1:
                matrix[i][j] = Node((j, i), True)
            else:
                matrix[i][j] = Node((j, i), False)
    return matrix


def node(x, y, matrix): 
    return matrix[y][x]


def drawChecks(checks, matrix):
    for x, y in checks:
        matrix[y][x] = "\U0001F7E8"

    return matrix


def drawMatrix(matrix, passes=None, res = ""):
    print(size(matrix))
    checks = passes[0]
    path = passes[1]
    matrix = drawChecks(checks, matrix)
    matrix = drawPath(path, matrix)
    

    for i, y in enumerate(matrix):
        for j, x in enumerate(y):
            if x == 1:
                y[j] = "\U0001F7EA"
            if x == 0:
                y[j] = "  "
            res += y[j]
        res += "\n"
    
    print(res)
    print(f"Shortest path: {len(path)-1} steps")


def size(matrix):
    return f"{len(matrix[0])-2} x {len(matrix)-2}"


def drawPath(path, matrix):
    for x, y in path:
        matrix[y][x] = "\U0001F7E6"
    start, end = path[-1], path[0]
    matrix[start[1]][start[0]] = "\U0001F7E5"
    matrix[end[1]][end[0]] = "\U0001F7E9"

    return matrix


def backtrack(log, start):
    backtracking = True
    current = log[-1]
    path_nodes = [current]
    path = [current[0]]
    checks = []
    for i in log:
        checks.append(i[0])
    
    while backtracking:
        if current[1] == start.pos:
            path.append(current[1])
            backtracking = False

        for i in log:
            if i[0] == current[1]:
                path_nodes.append(i)
                current = i
                checks.remove(i[0])
                path.append(i[0])

    return [checks, path]


def heuristic(current, goal, type):
    if type == "euclidean":
        return ceil(sqrt((current.x - goal.x)**2 + (current.y - goal.y)**2))
    elif type == "manhattan":
        return ceil((current.x - goal.x)**2 + (current.y - goal.y)**2)


def getGraph():
    return json.loads(open("src\graph.json", "r").read())


def solve(start, end, algorithm):
    matrix = getGraph()
    src_matrix_copy = deepcopy(matrix)
    matrix = convertMatrix(matrix)
    start = node(start[0], start[1], matrix)
    end = node(end[0], end[1], matrix)
    return algorithm(start, end, src_matrix_copy, matrix)


def viewGraph(graph, res = ""):
    for i, y in enumerate(graph):
        for j, x in enumerate(y):
            if x == 1:
                y[j] = "\U0001F7EA"
            if x == 0:
                y[j] = "  "
            res += y[j]
        res += "\n"
    print(size(graph))
    print(res)


def createGraph(x, y):
    matrix = []
    for i in range(y):
        matrix.append([])
    for i in range(x):
        matrix[0].append(1)
        matrix[-1].append(1)
    for i in matrix:
        if len(i) > 1:
            continue
        i.append(1)
    for i in matrix:
        if len(i) == x:
            continue
        for j in range(x-2):
            i.append(0)
        if len(i) == x-1:
            i.append(1)
    
    res = "[\n    "
    for i in matrix:
        if i is not matrix[-1]:
            res += f"{i},\n    "
        else:
            res += f"{i}\n"
            res += "]"
    open("src/graph.json", "w").write(res)
    print(f"Your graph has been created with size: {x} x {y}")
    print(f"Graph has been saved to graph.json")
    viewGraph(matrix)
    
    