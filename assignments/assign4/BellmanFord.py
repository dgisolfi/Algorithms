#!/usr/bin/env python3
# 2019-5-3

import math

class BellmanFord:
    def __init__(self, graph, vertex):
        self.__graph = graph
        self.__source_vertex = vertex
        # self.__source_weight = weight
        self.initSingleSource(self.__graph, self.__source_vertex)
        self.exploreVerticies()
        print(self.CheckForCircularPaths())

    def __str__(self):
        # convert float back to int here to make it look nicer
        for vertex in self.__graph.vertices:
            path = ''
            v = vertex
            while v.predecessor is not None:
                path += f'{v.predecessor.id}'
                v = v.predecessor
                if v.id  != '1':
                    path += '<='
            
            if path == '':
                print(f'id: {vertex.id} distance:{int(vertex.distance)} path: to itself')
            else:
                print(f'id: {vertex.id} distance:{int(vertex.distance)} path: {path}')
        return ''

    def initSingleSource(self, graph, source_vertex):
        for vertex in graph.vertices:
            # estimate of shortest path distance
            vertex.distance = math.inf
            # previous vertex
            vertex.predecessor = None
        source_vertex.distance = 0

    def exploreVerticies(self):
        for i in range(1, len(self.__graph.vertices)-1):
            for edge in self.__graph.edges:
                self.improvePath(edge.source, edge.target, edge.weight)

    # This is the "Relax" function...that name is confusing though
    # the weight is the weight of the edge between the to vertices
    def improvePath(self, test_vertex, best_vertex, weight):
        test_vertex = self.__graph.getVertex(test_vertex)
        best_vertex = self.__graph.getVertex(best_vertex)
        # the reason the weight and distance are casted to float 
        # is so later we can compare infinity to any value
        if best_vertex.distance > (test_vertex.distance + float(weight)):
            best_vertex.distance = float(test_vertex.distance + int(weight))
            best_vertex.predecessor = test_vertex
    

    def CheckForCircularPaths(self):
        for edge in self.__graph.edges:
            source = self.__graph.getVertex(edge.source)
            target = self.__graph.getVertex(edge.target)
            if source.distance > target.distance + float(edge.weight):
                return 'The Bellman-Ford Single-Source Shortest Path Algorithm cannot be completed on this graph'
            else:
                return 'done'
        