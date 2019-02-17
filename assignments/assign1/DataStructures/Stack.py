#!/usr/bin/env python3
# 2019-1-18

from .LinkedList import LinkedList

# A Python implementetation of a 
# Queue using a linked list
class Stack:
    def __init__(self):
        self.__stack = LinkedList()

    def __str__(self):
        return str(self.__stack)

    def __repr__(self):
        return self.__stack.__repr__()

    def __del__(self):
        self.__stack = None
        
    @property
    def stack(self):
        return self.__stack

    # Inserts an object at the top of the Stack.
    def push(self, element):
        self.__stack.addNode(element)

    # Removes and returns the object at the top of the Stack.
    def pop(self):
        return self.__stack.delNewestNode()

    # Returns the object at the top of the Stack without removing it.
    def peek(self):
        return self.__stack.head.data

    def clear(self):
        self.__stack = LinkedList()
    
    def length(self):
        return self.__stack.length()