#!/usr/bin/env python3
# 2019-3-29

class Vertex:
    def __init__(self, identifier):
        self.__id = identifier
        self.__connections = []

    ''' Properties '''
    @property
    def id(self):
        return self.__id
    
    @id.setter
    def setId(self, new_id):
        self.__id = new_id

    @property
    def connections(self):
        return self.__connections
    
    # @connections.setter
    def addConnection(self, vertex):
        self.__connections.append(vertex)

    @property
    def degree(self):
        return len(self.__connections)
    