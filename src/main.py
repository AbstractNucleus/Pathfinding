from general import createGraph, getGraph, solve, viewGraph
from a_star import aStar
from dijkstras import dijkstras


graph = getGraph()
start = (24, 11)
end = (30, 13)


#createGraph(50, 25)
#viewGraph(graph)
solve(start, end, aStar)