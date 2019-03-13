#!/usr/bin/env python3
# 2019-2-17

import math

class BinarySearch:
    def __init__(self, elements, desired_item):
        self.elements = elements
        self.desired_item = desired_item
        self.__comparisons = 0
    
    @property
    def comparisons(self):
        return self.__comparisons

    def search(self):
        found = False
        midpoint = 0
        # Lower Bound
        low = 0 
        # Upper Bound
        high = len(self.elements) - 1
        # While there is still elements 
        # in this range, keep looking
        while low <= high and not found: 
            # find the midpoint based on the upper and 
            # lower bounds of the section of the arrsay 
            # we are looking at
            midpoint = math.floor((low + high)/ 2)
            
            self.__comparisons += 2
            if self.elements[midpoint] < self.desired_item:
                self.__comparisons -= 1
                low = midpoint + 1
            elif self.elements[midpoint] > self.desired_item:
                # This is the 2nd comaprisons because it
                # took two comparisons to get into this scope
                high = midpoint - 1
            else:
                # add two here as the last two comparisons were not counted
                # The midpoint IS the desired item
                # return the index it was found at
                found = True

        return midpoint