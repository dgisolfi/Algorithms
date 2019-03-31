#!/usr/bin/env python3
# 2019-3-31

import sys
from parser import Parser
sys.path.append('.')
from LinkedObjectGraph.ObjectGraph import ObjectGraph

parser = Parser('./test/graphs.txt')

for graph in parser.graph_commands:
    print('NEW GRAPH')
    objectGraph = ObjectGraph(graph)
    print(objectGraph)
    print('-----------------------')
