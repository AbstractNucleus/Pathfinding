import ast
from general import createGraph, getGraph, solve, viewGraph, randomwalls
from a_star import aStar
from dijkstras import dijkstras


#def randomwalls(graph):

graph = getGraph()
start = (10,10)
end = (60, 30)
#graph = randomwalls(graph)


#createGraph(70, 40)
#viewGraph(graph)
solve(graph, start, end, aStar)
