#!/usr/bin/env python3
# 2019-1-18

from .LinkedList import LinkedList

class HashTable:
    def __init__(self, size):
        self.__table = [None] * size
        self.__keys = []
        self.__comparisons = 0

    def __repr__(self):
        return str(self.__table)
    
    ''' Propertys '''
    @property
    def isEmpty(self):
        if len(self.__table) is 0:
            return True
        else:
            return False

    @property
    def comparisons(self):
        return self.__comparisons

    @comparisons.setter
    def setComparisons(self, val):
        self.__comparisons = val

    @property
    def keys(self):
        return self.__keys

    @property
    def size(self):
        return len(self.__table)

    ''' Methods '''
    def get(self, obj):
        key = self.__findKey(obj)
        value = self.__table[key]
        # Traverse the linked list and return the object found there
        if value is not None:
            node = value.head
            while node is not None:
                self.__comparisons += 1
                if node == obj:
                    return node.data
                else:
                    node = node.pointer
    
    # Returns the key where it was placed
    def put(self, value):
        # get the key for the given value
        key = self.__findKey(value)
        # Check if the table[key] has a linked list yet
        if self.__table[key] is None:
            # Theres not a linked list there
            self.__table[key] = LinkedList()
           
        # Now add to the linked list
        self.__table[key].addNode(value)
        return key

    def remove(self, key):
        # Remove and return value of key
        value = self.get(key)
        self.__table[key] = None
        return value

    ''' Private Methods '''
    def __findKey(self, value):
        if self.isEmpty:
            return None
        # A nice dash of functional programming
        key = int(sum(ord(ch) for ch in value) % self.size)
        return key 