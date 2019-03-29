#!/usr/bin/env python3
# 2019-3-29

import re
import sys
sys.path.append('.')
from DataStructures.graph import Graph

class Parser:
    def __init__(self, filename):
        self.filename = filename
        self.__graphs = []
        self.__commands = []
        self.parse()
        
    ''' Propertys '''
    @property
    def graphs(self):
        return self.__graphs

    @property
    def commands(self):
        return self.__commands

    ''' Methods '''
    def getCmds(self, filename):
        try:
            file = open(filename, 'r')
            commands = file.readlines()
            file.close()
            return commands
        except Exception as e:
            print(f'Error: {e}')
    
    def removeComments(self):
        self.__commands = [re.sub(r'\n', '', line) for line in self.__commands]
        self.__commands = [re.sub(r'^--.*$', '', line) for line in self.__commands]
        
        
    def parse(self):
        # Get all commands from the file
        self.__commands = self.getCmds(self.filename)
        # Remove the comments and line breaks from the commands
        self.removeComments()

        for cmd in self.__commands:
            if re.match(r'new graph', cmd):
                if 'graph' in locals():
                    self.__graphs.append(graph)
                graph = Graph()
            elif re.match(r'add vertex .*', cmd):
                try:
                    vertex_val = re.sub(r'add vertex', '', cmd)
                    graph.addVertex(vertex_val)
                except UnboundLocalError:
                    print('You must define a new graph before adding a vertex.')
            
            elif re.match(r'add edge .*', cmd):
                try:
                    edge_vals = re.sub(r'add edge', '', cmd)
                    values = edge_vals.split('-')
                    graph.addEdge(values[0], values[1])
                except UnboundLocalError:
                    print('You must define a new graph before adding an edge.')
