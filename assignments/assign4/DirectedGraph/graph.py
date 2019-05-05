#!/usr/bin/env python3
# 2019-5-3

from .vertex import Vertex
from .edge import Edge

class Graph:
    def __init__(self):
        self.__vertices = []
        self.__edges = []

    ''' Properties '''
    @property
    def vertices(self):
        return self.__vertices
    
    @vertices.setter
    def vertices(self, vertices):
        self.__vertices = vertices

    @property
    def edges(self):
        return self.__edges

    @edges.setter
    def edges(self, edges):
        self.__edges = edges
        
    ''' Methods '''
    def addVertex(self, identifier):
        self.__vertices.append(Vertex(identifier))
    
    def getVertex(self, identifier):
        for vertex in self.__vertices:
            if vertex.id == identifier:
                return vertex

    def addEdge(self, source, target, weight):
        self.edges.append(Edge(source, target, weight))

    # def addEdge(self, vertex_1, vertex_2, weight):
    #     self.getVertex(vertex_1).addConnection(self.getVertex(vertex_2))
    #     self.getVertex(vertex_2).addConnection(self.getVertex(vertex_1))
    #     self.__edges.append(f'{vertex_1}=>{vertex_2} weight={weight}')
