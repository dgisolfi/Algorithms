#!/usr/bin/env python3
# 2019-3-29

from .vertex import Vertex

class Graph:
    def __init__(self):
        self.__vertices = []

    ''' Properties '''
    @property
    def vertices(self):
        return self.__vertices
        
    ''' Methods '''
    def addVertex(self, identifier):
        self.__vertices.append(Vertex(identifier))
    
    def getVertex(self, identifier):
        for vertex in self.__vertices:
            # print(vertex.id, identifier, vertex.id == identifier)
            if vertex.id == identifier:
                return vertex

    def addEdge(self, vertex_1, vertex_2):
        self.getVertex(vertex_1).addConnection(vertex_2)
        self.getVertex(vertex_2).addConnection(vertex_1)
