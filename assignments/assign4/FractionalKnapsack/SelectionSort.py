#!/usr/bin/env python3
# 2019-2-17

class SelectionSort:
    def __init__(self, elements):
        self.__elements = elements
        self.__comparisons = 0
        self.sort()

    @property
    def comparisons(self):
        return self.__comparisons

    @property
    def elements(self):
        return self.__elements
    
    @elements.setter
    def elements(self, elements):
        self.__elements = elements

    def sort(self):
        node = self.elements.head

        while node is not None:
            # The current element is the new minimum
            minimum = node

            # loop through remaining elements of the list
            next_node = node.pointer

            while next_node is not None:
                # check if the next item is lower the the current minimum
                if next_node.data.price > minimum.data.price:
                    minimum = next_node
                next_node = next_node.pointer

            # check if the minimum changed, if so swap
            if minimum.data.price != node.data.price:
                self.elements.swap(node, minimum)

            node = node.pointer