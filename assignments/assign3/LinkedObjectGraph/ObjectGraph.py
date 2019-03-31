#!/usr/bin/env python3
# 2019-3-31

import re
from .graph import Graph


class ObjectGraph:
    def __init__(self, commands):
        self.commands = commands
        self.graph = Graph()
        self.buildGraph()

    def __str__(self):
        self.depthFirstTraversal()
        return ''
    

    def buildGraph(self):
        for cmd in self.commands:
            if re.match(r'add vertex .*', cmd):
                try:
                    identifier = re.sub(r'add vertex', '', cmd)
                    self.graph.addVertex(identifier.strip())
                except UnboundLocalError:
                    print('You must define a new graph before adding a vertex.')
            
            elif re.match(r'add edge .*', cmd):
                try:
                    edge_vals = re.sub(r'add edge', '', cmd)
                    values = edge_vals.split('-')
                    self.graph.addEdge(values[0].strip(), values[1].strip())
                except UnboundLocalError:
                    print('You must define a new graph before adding an edge.')


    def depthFirstTraversal(self):
        for vertex in self.graph.vertices:
            print(f'[{vertex.id}]')
            for conn in vertex.connections:
                print(f'\t{conn}')