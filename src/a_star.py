from general import getNeighboors, drawMatrix, backtrack, heuristic
import random

def getCurrent(open_set, end):
    f_costs = []
    for node in open_set:
        if node.parent != None:
            node.g = 1 + node.parent.g
            node.h = heuristic(node, end, "manhattan")
            node.f = node.g + node.h
        f_costs.append(node.f)

    return open_set[f_costs.index(min(f_costs))]


def aStar(start, end, src_matrix_copy, matrix):
    open_set, closed_set = [start], []
    log = []

    while True:
        current = getCurrent(open_set, end)
        open_set.remove(current)
        closed_set.append(current)

        if current != start:
            log.append([current.pos, current.parent.pos])
        
        if current == end:
            break

        for neighboor in getNeighboors(current, matrix):
            if (neighboor.wall == True) or (neighboor in closed_set):
                continue

            if (current.g < neighboor.g) or (neighboor not in open_set):
                if neighboor not in open_set:
                    neighboor.parent = current
                    open_set.append(neighboor)  

    return drawMatrix(src_matrix_copy, backtrack(log, start))





        
