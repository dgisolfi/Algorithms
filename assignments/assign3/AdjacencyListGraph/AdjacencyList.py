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
            print(f'{vertex}\t {self.__graph[vertex]}')
        return ''
    
    def buildList(self):
        for cmd in self.__commands:
            if re.match(r'add vertex .*', cmd):
                try:
                    identifier = re.sub(r'add vertex', '', cmd)
                    self.__graph[identifier.strip()] = set()
                except UnboundLocalError:
                    print('You must define a new graph before adding a vertex.')
            
            elif re.match(r'add edge .*', cmd):
                try:
                    edge_vals = re.sub(r'add edge', '', cmd)
                    values = edge_vals.split('-')
                    self.__graph[values[0].strip()].add(values[1].strip())
                    self.__graph[values[1].strip()].add(values[0].strip())
                except UnboundLocalError:
                    print('You must define a new graph before adding an edge.')