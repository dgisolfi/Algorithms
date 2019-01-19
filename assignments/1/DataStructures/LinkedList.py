#!/usr/bin/env python3
# 2019-1-18

from .Node import Node

# A Python implementetation of a 
# singly linked list
class LinkedList:
    def __init__(self):
        # First Node in list is the HEAD
        # it moves to be the most recent one
        self.__head = None

    def __str__(self):
        visual = ''
        node = self.__head
        while(node):
            visual += f'{node.data}=>'
            node = node.pointer
        return f'{visual}Null'
        
    def __repr__(self):
        return f'{self.__class__}({self})'

    @property
    def head(self):
        return self.__head

    @head.setter
    def head(self, node):
        self.__head = node

    @head.deleter
    def head(self, node):
        del self.__head

    def addNode(self, element):
        # Each node should point to the next node
        new_node = Node(data=element, pointer=self.head)
        self.__head = new_node

    # Returns the deleted value, the most recent node added
    # AKA the Head
    def delNewestNode(self):
        node = self.head
        self.head = node.pointer
        return node.data

     # Delete First Node in list(the one pointing to Null)
    def delOldestNode(self):
        oldest_node = object
        node = self.__head
        prev_node = node
        while(node):
            if node.pointer is None:
                oldest_node = node
                if prev_node is not None:
                    prev_node.pointer = None
                return oldest_node.data
            prev_node = node
            node = node.pointer

    def length(self):
        size = 0
        # List Empty
        if self.__head is None:
            return size
        node = self.__head
        while node.pointer is not None:
            size += 1
            node = node.pointer
        
        # The head needs to be counted to
        # but has a Null val for its pointer
        if node.data is not None:
            size += 1
        return size