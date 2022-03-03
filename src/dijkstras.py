from general import getNeighboors, drawMatrix, backtrack


def getCurrent(open_set):
    g_costs = []
    for node in open_set:
        if node.parent != None:
            node.g = 1 + node.parent.g
        g_costs.append(node.g)

    return open_set[g_costs.index(min(g_costs))]


def dijkstras(start, end, src_matrix_copy, matrix):
    open_set, closed_set = [start], []
    log = []

    while True:
        current = getCurrent(open_set)
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





        
