#!/usr/bin/env python3
# 2019-1-18

# A Python implementetation of a Node class
class Node:
    def __init__(self, data, pointer, previous):
        self.__data = data
        self.__pointer = pointer
        self.__previous = previous
    
    @property
    # data => Element to be stored
    def data(self):
        return self.__data

    @data.setter
    def data(self, element):
        self.__data = element
    
    @property
    # pointer => next element in linked list
    def pointer(self):
        return self.__pointer

    @pointer.setter
    def pointer(self, obj):
        self.__pointer = obj

    @property
    def previous(self):
        return self.__previous

    @previous.setter
    def previous(self, obj):
        self.__previous = obj
