#!/usr/bin/env python3
# 2019-5-1

import sys
sys.path.append('..')
from assign4.parser import Parser
from assign4.DirectedGraph.DirectedGraph import DirectedGraph

parser = Parser('./test/graphs2.txt')

for graph in parser.graph_commands:
    print('NEW GRAPH')
    directedGraph = DirectedGraph(graph)
    print(directedGraph)
    print('-----------------------')
