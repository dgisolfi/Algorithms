#!/usr/bin/env python3
# 2019-2-17

class MergeSort:
    def __init__(self, elements):
        self.elements = elements
        self.__comparisons = 0

    @property
    def comparisons(self):
        return self.__comparisons

    def sort(self):
        return self.mergeSort(self.elements)

    def mergeSort(self, items):
        # We dont need to sort an empty list or list with 1 element
        if len(items) is 1 or len(items) is 0:
            return items
        # Split the array in half
        array_1 = items[:int(len(items)/2)]
        # Add 1 to avoid an imperfect split
        array_2 = items[int(len(items)/2):]

        # Preform a merge sort on the split arrays
        array_1 = self.mergeSort(array_1)        
        array_2 = self.mergeSort(array_2)  

        return self.merge(array_1, array_2)


    def merge(self, a, b):
        results = []
        # for all elements compare the zeroth value 
        # and add the lower element to the results, 
        # removing the element afterwards
        while len(a) > 0 and len(b) > 0:
            self.__comparisons += 1
            if a[0].lower() > b[0].lower():
                results.append(b[0])
                del b[0]
            else:
                results.append(a[0])
                del a[0]
        
        # One of the arrays will still have items,
        # They are already in order tho so just add them
        while len(a) > 0:
            results.append(a[0])
            del a[0]

        while len(b) > 0:
            results.append(b[0])
            del b[0]

        return results