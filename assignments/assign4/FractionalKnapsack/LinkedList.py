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
        self.__tail = None

    def __str__(self):
        visual = ''
        node = self.__head
        while(node):
            visual += f'{node.data}=>'
            node = node.pointer
        return f'{visual}Null'
        
    def __repr__(self):
        return str(self)

    @property
    def head(self):
        return self.__head

    @head.setter
    def head(self, node):
        self.__head = node

    @head.deleter
    def head(self, node):
        del self.__head

    @property
    def tail(self):
        return self.__tail

    @tail.setter
    def tail(self, node):
        self.__tail = node

    @tail.deleter
    def tail(self, tail):
        del self.__tail

    @property
    def length(self):
        return self.__length()

    def append(self, element):
        # Each node should point to the next node
        node = Node(data=element, pointer=self.head, previous=None)
        if self.head is not None:
            self.head.previous = node
        self.head = node
        if self.head.pointer is None:
            self.tail = self.head

    # Returns the deleted value, the most recent node added
    # AKA the Head
    def deleteHead(self):
        node = self.head
        self.head = node.pointer
        return node.data

     # Delete First Node in list(the one pointing to Null)
    def deleteTail(self):
        oldest_node = object
        node = self.__head
        prev_node = node
        while(node):
            if node.pointer is None:
                oldest_node = node
                if prev_node is not None:
                    prev_node.pointer = None
                    self.tail = prev_node
                return oldest_node.data
            prev_node = node
            node = node.pointer

    def __length(self):
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

    def swap(self, node_1, node_2):
        temp = node_1.data
        node_1.data = node_2.data
        node_2.data = temp
        # node_1_temp = node_1
        # node_2_temp = node_2

        # node_1 = node_2_temp
        # node_1.pointer = node_1_temp.pointer
        # node_1.previous = node_1_temp.previous
            
        # node_2 = node_1_temp
        # node_2.pointer = node_2_temp.pointer
        # node_2.previous = node_2_temp.previous