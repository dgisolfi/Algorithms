#!/usr/bin/env python3
# 2019-4-16

''' 
NOTICE: This is an implementation using the Hashmap from assignment 2. 
I prefer the other but just in case alan prefers this, I added it.
''' 

import re
from .HashTable import HashTable

class AdjacencyList:
    def __init__(self, commands):
        self.__commands = commands
        # In this case we want each entry to be its own vertex,
        # so find the num of vertices to make the table
        vertices = len(re.findall('add vertex', ''.join(self.__commands)))+1

        self.__graph = HashTable(vertices)
        self.buildList()
    
    def __str__(self):
        for vertex in self.__graph.keys:
            value = self.__graph.get(int(vertex))
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
                # I guess theres nothing to do here...
       
            
            elif re.match(r'add edge .*', cmd):
                edge_vals = re.sub(r'add edge', '', cmd)
                values = edge_vals.split('-')
                self.__graph.put(values[0].strip(), values[1].strip())
                self.__graph.put(values[1].strip(), values[0].strip())