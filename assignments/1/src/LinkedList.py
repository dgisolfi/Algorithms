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
    def delNode(self):
        temp = self.__head
        self.__head = self.__head.pointer
        return temp

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


test = LinkedList()
test.addNode('node')
test.addNode('node2')
test.addNode('node3')
print(test.length())
print(test.head.data)
print(test.head)

print((test.delNode()).data)
print(test.length())