#!/usr/bin/env python3
# 2019-5-1

import sys
sys.path.append('..')
from assign4.parser import Parser
from assign4.DirectedGraph.DirectedGraph import DirectedGraph
from assign4.BellmanFord import BellmanFord

parser = Parser('./test/graphs2.txt')

for cmds in parser.graph_commands:
    print('NEW GRAPH')
    directedGraph = DirectedGraph(cmds)
    print(directedGraph)
    graph = directedGraph.graph

    bellmanFord = BellmanFord(graph, graph.vertices[0])
    print(bellmanFord)


