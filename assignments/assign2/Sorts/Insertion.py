#!/usr/bin/env python3
# 2019-2-17

class InsertionSort:
    def __init__(self, elements):
        self.elements = elements
        self.__comparisons = 0

    @property
    def comparisons(self):
        return self.__comparisons

    def sort(self):
        # Loop through all elements of the array
        for item in range(1,len(self.elements)):
            # save the current element and make comparisons
            # Make lowercase otherwise Z > a
            temp = self.elements[item].lower()
            prev_item = item
            # compare the temp to all values.
            while prev_item > 0 and self.elements[prev_item-1].lower() > temp:
                # Swap the compared elements
                self.elements[prev_item] = self.elements[prev_item-1]
                self.__comparisons += 1  
                prev_item -= 1
            # Return the stored element to the list
            self.elements[prev_item] = temp
        return self.elements