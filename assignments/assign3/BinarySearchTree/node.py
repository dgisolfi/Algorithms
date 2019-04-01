#!/usr/bin/env python
# 2019-3-31

class Node:
    def __init__(self, value=None):
        self.__value = value
        self.__left_child = None
        self.__right_child = None

    @property
    def value(self):
        return self.__value

    @property
    def left_child(self):
        return self.__left_child
    
    @property
    def right_child(self):
        return self.__right_child

    def setLeftChild(self, child):
        self.__left_child = child

    def setRightChild(self, child):
        self.__right_child = child


