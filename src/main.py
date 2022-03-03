from general import createGraph, getGraph, solve, viewGraph
from a_star import aStar
from dijkstras import dijkstras


graph = getGraph()
start = (1, 1)
end = (80, 45)


#createGraph(100, 50)
#viewGraph(graph)
solve(start, end, aStar)