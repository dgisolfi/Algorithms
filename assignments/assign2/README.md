 # Assignment 2

**Daniel Gisolfi**

## Sorts

### Insertion Sort

```python
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
```

### Selection Sort 

```python
#!/usr/bin/env python3
# 2019-2-17

class SelectionSort:
    def __init__(self, elements):
        self.elements = elements
        self.__comparisons = 0

    @property
    def comparisons(self):
        return self.__comparisons

    def sort(self):
        for item in range(0,len(self.elements)-1):
            # The current element is the new minimum
            minimum = item
            # Start the loop by looking at the next element
            i = minimum + 1
            while i < len(self.elements):
                # Check if the (lower case version) next item is lower then the current min
                self.__comparisons += 1
                if self.elements[i].lower() < self.elements[minimum].lower():
                    minimum = i
                i += 1
            
            # If the minimum has changed preform a swap
            if minimum is not item:
                temp = self.elements[item]
                self.elements[item] = self.elements[minimum]
                self.elements[minimum] = temp

        return self.elements
```

### Merge Sort

```python
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
```

### Quick Sort

```python
#!/usr/bin/env python3
# 2019-2-17

class QuickSort:
    def __init__(self, elements):
        self.elements = elements
        self.__comparisons = 0

    @property
    def comparisons(self):
        return self.__comparisons 

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
            self.__comparisons += 1
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
        return arr
```

|   Sort    | Comparisons |             Asymptotic              |
| :-------: | :---------: | :---------------------------------: |
| Insertion |   114309    |        Ω(n) ϴ(n^2^) O(n^2^)         |
| Selection |   221445    |       Ω(n^2^) ϴ(n^2^) O(n^2^)       |
|   Merge   |    5413     | Ω(n log(n)) ϴ(n log(n)) O(n log(n)) |
|   Quick   |    6490     |   Ω(n log(n)) ϴ(n log(n)) O(n^2^)   |

**Insertion** - The best case is when the list is already sorted and so has a running time of n. The average and worst case then occurs when an element is out of place so every element has to be checked for every place in the list.

**Selection** - No matter what selection sort will scan all elements of the list in order to place them in the correct order comparing to all other values making this a n^2^ operation.

**Merge** - In it's average and worst case the complexity becomes splitting the list and adding n steps taken to merge the resulting two lists this is an operation of O(n log(n)).

**Quick** - in its implementation each call only takes O(n) plus 2 recursive calls on a list of n/2, the best and average case is O(n log(n)) while worse can be O(n^2^)

## Searches

### Linear

```python
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
        itemNotFound = True
        index = 0
        while itemNotFound:
            item = self.elements[index]
            self.__comparisons += 1
            if item is self.desired_item:
                itemNotFound = False
            else:
                index += 1

        return index
```

### Binary

```python
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
            
            if self.elements[midpoint] < self.desired_item:
                self.__comparisons += 1
                low = midpoint + 1
            elif self.elements[midpoint] > self.desired_item:
                # This is the 2nd comaprisons because it
                # took two comparisons to get into this scope
                self.__comparisons += 2
                high = midpoint - 1
            else:
                # add two here as the last two comparisons were not counted
                self.__comparisons += 2
                # The midpoint IS the desired item
                # return the index it was found at
                found = True

        return midpoint
```
|   Searches   | Comparisons |             Asymptotic              |
| :-------: | :---------: | :---------------------------------: |
| Linear |     334     |  Ω(n) ϴ(n^2^) O(n^2^)  |
|  Binary  |     11      | Ω(n) ϴ(log n) O(log n) |

**linear** - this is a simple search wherein no matter what all elements are checked to find the element in the best case on say a sorted list the complexity can be just n while usually, the case is that the search is double that at n^2^

**BInary** - The average and worst-case scenarios or wherein less than half the elements must be searched due to divide and conquer while at its worst the search must look through the entire list 

## Data Stuctures

### HashTable

```python
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
```



| Data Stuctures | Comparisons |   Asymptotic   |
| :------------: | :---------: | :------------: |
|   Hash Table   |      5      | Ω(1) ϴ(1) O(n) |

**Hash Table** - In its best case the first get is the element we are searching for, this is also the average case. However, in its worst case, it takes n lookups to find the element due to searching through linked lists