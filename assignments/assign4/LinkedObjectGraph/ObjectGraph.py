#!/usr/bin/env python3
# 2019-3-31

import re
from .graph import Graph

class ObjectGraph:
    def __init__(self, commands):
        self.__commands = commands
        self.__graph = Graph()
        self.__viewed = []
        self.buildGraph()

    def __str__(self):
        print('----vertices---')
        [print(vertex.id) for vertex in self.__graph.vertices]
        print('-----edges-----')
        [print(edge) for edge in self.__graph.edges]
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
                self.__graph.addVertex(identifier.strip())
            
            elif re.match(r'add edge .*', cmd):
                edge_vals = re.sub(r'add edge', '', cmd)
                values = edge_vals.split('-')
                second_value = values[1].split(' ')
                values[1] = second_value[1]
                weight = second_value[2]
                self.__graph.addEdge(values[0].strip(), values[1].strip(), weight)
