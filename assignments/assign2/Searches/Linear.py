#!/usr/bin/env python3
# 2019-2-17

class LinearSearch:
    def __init__(self, elements, desired_item):
        self.elements = elements
        self.desired_item = desired_item
        self.__comparisons = 0
    
    @property
    def comparisons(self):
        return self.__comparisons
    
    def search(self):
        for index, item in enumerate(self.elements):
            self.__comparisons += 1
            if item is self.desired_item:
                return index
