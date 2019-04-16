#!/usr/bin/env python3
# 2019-3-31

import re

class AdjacencyList:
    def __init__(self, commands):
        self.__commands = commands
        self.__graph = {}
        self.buildList()
    
    def __str__(self):
        for vertex in self.__graph:
            value = self.__graph[vertex]
            if len(value) is 0:
                value = '{}'
            print(f'{vertex}\t {value}')
        return ''

    ''' Properties '''
    @property
    def adjacencyList(self):
        return self.__graph

    ''' Methods '''
    def buildList(self):
        for cmd in self.__commands:
            if re.match(r'add vertex .*', cmd):
                identifier = re.sub(r'add vertex', '', cmd)
                self.__graph[identifier.strip()] = set()
            
            elif re.match(r'add edge .*', cmd):
                edge_vals = re.sub(r'add edge', '', cmd)
                values = edge_vals.split('-')
                self.__graph[values[0].strip()].add(values[1].strip())
                self.__graph[values[1].strip()].add(values[0].strip())