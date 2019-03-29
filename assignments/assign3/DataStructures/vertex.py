#!/usr/bin/env python3
# 2019-3-29

class Vertex:
    def __init__(self, point):
        self.__value = point

    ''' Propertys '''
    @property
    def value(self):
        return self.__value
    
    @value.setter
    def setValue(self, new_value):
        self.__value = new_value