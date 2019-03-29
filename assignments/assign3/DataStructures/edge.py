#!/usr/bin/env python3
# 2019-3-29

class Edge:
    def __init__(self, source, destination):
        self.__source = source
        self.__destination = destination

    ''' Propertys '''
    @property
    def source(self):
        return self.__source

    @source.setter
    def setSource(self, new_source):
        self.__source = new_source

    @property
    def destination(self):
        return self.__destination

    @destination.setter
    def setDestination(self, new_destination):
        self.__destination = new_destination
    