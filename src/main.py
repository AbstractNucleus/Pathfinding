import ast
from general import createGraph, getGraph, solve, viewGraph, randomwalls
from a_star import aStar
from dijkstras import dijkstras


#def randomwalls(graph):

graph = getGraph()
start = (1, 1)
end = (48, 48)
#graph = randomwalls(graph)


#createGraph(50, 50)
#viewGraph(graph)
solve(graph, start, end, dijkstras)
