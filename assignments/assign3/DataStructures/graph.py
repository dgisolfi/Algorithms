#!/usr/bin/env python3
# 2019-3-29

from .vertex import Vertex
from .edge import Edge

class Graph:
    def __init__(self):
        self.__vertices = []
        self.__edges = []

    ''' Propertys '''
    @property
    def vertices(self):
        return self.__vertices
    
    @property
    def edges(self):
        return self.__edges
        
    ''' Methods '''
    def addVertex(self, value):
        self.__vertices.append(Vertex(value))
    
    def addEdge(self, vertex_1, vertex_2):
        self.__edges.append(Edge(vertex_1, vertex_2))
    