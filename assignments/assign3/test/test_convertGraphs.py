#!/usr/bin/env python3
# 2019-3-31

import sys
from parser import Parser
sys.path.append('.')

from LinkedObjectGraph.ObjectGraph import ObjectGraph
from AdjacencyListGraph.AdjacencyList import AdjacencyList
from MatrixGraph.Matrix import Matrix

parser = Parser('./test/graphs.txt')

graph_num = 1
for graph in parser.graph_commands:
    print(f'Graph {graph_num}')
    print('Adjacency List')
    adjacencyList = AdjacencyList(graph)
    print(adjacencyList)
    print('Matrix')
    matrix = Matrix(graph)
    print(matrix)
    print('Linked Object Traversal')
    objectGraph = ObjectGraph(graph)
    print(objectGraph)
    print('-----------------------')
    graph_num += 1 