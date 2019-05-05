#!/usr/bin/env python3
# 2019-5-3

class Vertex:
    def __init__(self, identifier):
        self.__id = identifier
        self.__distance = None
        self.__predecessor = None

    ''' Properties '''
    @property
    def id(self):
        return self.__id
    
    @id.setter
    def setId(self, new_id):
        self.__id = new_id

    # @property
    # def degree(self):
    #     return len(self.__connections)

    @property
    def distance(self):
        return self.__distance
    
    @distance.setter
    def distance(self, dist):
        self.__distance = dist

    @property
    def predecessor(self):
        return self.__predecessor

    @predecessor.setter
    def predecessor(self, predecessor):
        self.__predecessor = predecessor
    