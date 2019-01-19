#!/usr/bin/env python3
# 2019-1-18

from .LinkedList import LinkedList

# A Python implementetation of a 
# Queue using a linked list
class Queue:
    def __init__(self, *args, **kwargs):
        self.__queue = LinkedList()

    def __str__(self):
        return str(self.__queue)
    
    def __repr__(self):
        return self.__queue.__repr__()

    def __del__(self):
        self.__queue = None

    @property
    def queue(self):
        return self.__queue
    
    def enqueue(self, element):
        self.__queue.addNode(element)

    def dequeue(self):
        return self.__queue.delOldestNode()

    def length(self):
        return self.__queue.length

    