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
        print('Depth First Traversal')
        self.depthFirstTraversal(self.__graph.vertices[0])
        print('Breadth First Traversal')
        self.breadthFirstTraversal(self.__graph.vertices[0])
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
                self.__graph.addEdge(values[0].strip(), values[1].strip())



    def depthFirstTraversal(self, node):
        for vertex in node.connections:
            if vertex.id not in self.__viewed:

                print(vertex.id)
                self.__viewed.append(vertex.id)
                self.depthFirstTraversal(vertex)


    def breadthFirstTraversal(self, node):
        q = [node]
        viewed = {}
        while len(q) is not 0:
            vertex = q.pop(0)
            marked = viewed.get(vertex.id, None)
            
            if marked is None:
                print(vertex.id)
                viewed[vertex.id] = True
            
            for conn in vertex.connections:
                marked = viewed.get(conn.id, None)
                if marked is not True:
                    q.append(conn)














