#!/usr/bin/env python3
# 2019-2-17

class SelectionSort:
    def __init__(self, elements):
        self.elements = elements

    def sort(self):
        for item in range(0,len(self.elements)-1):
            # The current element is the new minimum
            minimum = item
            # Start the loop by looking at the next element
            i = minimum + 1
            while i < len(self.elements):
                # Check if the (lower case version) next item is lower then the current min
                if self.elements[i].lower() < self.elements[minimum].lower():
                    minimum = i
                i += 1
            
            # If the minimum has changed preform a swap
            if minimum is not item:
                temp = self.elements[item]
                self.elements[item] = self.elements[minimum]
                self.elements[minimum] = temp

        return self.elements
                
