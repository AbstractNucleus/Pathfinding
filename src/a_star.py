from a_star_modules import *
from graph import src_matrix

matrix = convert_matrix(src_matrix)


def node(x, y): return matrix[y][x]


start = node(1,0)
end = node(16, 23)


def aStar(start, end):
    open = [start]
    closed = []
    finished = False
    print(get_neighboors(start, matrix)[2].pos)


aStar(start, end)

        
