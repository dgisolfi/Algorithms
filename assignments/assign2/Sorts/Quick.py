#!/usr/bin/env python3
# 2019-2-17

class QuickSort:
    def __init__(self, elements):
        self.elements = elements
        self.__swaps = 0

    @property
    def swaps(self):
        return self.__swaps 

    def sort(self):
        # Start by runing quicksort on the arr with the upper and 
        # lower bound... 0 and the length of the arr
        return self.quickSort(self.elements, 0, len(self.elements))

    def quickSort(self, items, low, high):

        # store the pivot and run quicksort on the left and right
        if low < high:
            # Pivot is used to find the upper and lower bounds of the partioned lists
            pivot = self.partition(items, low, high)
            items = self.quickSort(items, low, pivot)
            items = self.quickSort(items, pivot+1, high)
        # Give back the sorted list
        return items

    def partition(self, items, low, high):
        # lowest item is the pivet
        pivot = items[low]
        left = low

        # From left to right run comparisons on each
        for i in range(low+1,high):
            # Check the lowercase version and swap if needed
            if items[i].lower() < pivot.lower():
                items = self.swap(items, i, left)
                # We can move to the right by 1
                left += 1

        items = self.swap(items, items.index(pivot), left)
        return left

    # switch em
    def swap(self, arr, pos_1, pos_2):
        temp = arr[pos_1]
        arr[pos_1] = arr[pos_2]
        arr[pos_2] = temp
        self.__swaps += 1
        return arr