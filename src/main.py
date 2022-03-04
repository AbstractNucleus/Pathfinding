from general import createGraph, getGraph, solve, viewGraph, randomwalls
from a_star import aStar
from dijkstras import dijkstras
import random
import math

#def randomwalls(graph):

graph = getGraph()
start = (1,1)
end = (45, 23 )
graph = randomwalls(graph)


#createGraph(50, 25)
#viewGraph(graph)
solve(graph,start, end, aStar)
