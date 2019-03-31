#!/usr/bin/env python3
# 2019-3-31

import re
from .graph import Graph

class ObjectGraph:
    def __init__(self, commands):
        self.__commands = commands
        self.__graph = Graph()
        self.buildGraph()

    def __str__(self):
        self.depthFirstTraversal()
        return ''

    ''' Properties '''
    @property
    def graph(self):
        return self.__graph
    
    ''' Methods '''
    def buildGraph(self):
        for cmd in self.__commands:
            if re.match(r'add vertex .*', cmd):
                identifier = re.sub(r'add vertex', '', cmd)
                self.graph.addVertex(identifier.strip())
            
            elif re.match(r'add edge .*', cmd):
                edge_vals = re.sub(r'add edge', '', cmd)
                values = edge_vals.split('-')
                self.graph.addEdge(values[0].strip(), values[1].strip())


    def depthFirstTraversal(self):
        for vertex in self.graph.vertices:
            print(f'[{vertex.id}]')
            for conn in vertex.connections:
                print(f'\t{conn}')