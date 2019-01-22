#!/usr/bin/env python3
# 2019-1-18

# A Python implementetation of a Node class
class Node:
    def __init__(self, data, pointer):
        self.__data = data
        self.__pointer = pointer
    
    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, element):
        self.__data = element
    
    @property
    def pointer(self):
        return self.__pointer

    @pointer.setter
    def pointer(self, obj):
        self.__pointer = obj
