# Assignment 1

### Daniel Gisolfi

`Node.py`

```python
#!/usr/bin/env python3
# 2019-1-18

# A Python implementetation of a Node class
class Node:
    def __init__(self, data, pointer):
        self.__data = data
        self.__pointer = pointer
    
    @property
    # data => Element to be stored
    def data(self):
        return self.__data

    @data.setter
    def data(self, element):
        self.__data = element
    
    @property
    # pointer => next element in linked list
    def pointer(self):
        return self.__pointer

    @pointer.setter
    def pointer(self, obj):
        self.__pointer = obj
```

`LinkedList.py`

```python
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

    def __str__(self):
        visual = ''
        node = self.__head
        while(node):
            visual += f'{node.data}=>'
            node = node.pointer
        return f'{visual}Null'
        
    def __repr__(self):
        return f'{self.__class__}({self})'

    @property
    def head(self):
        return self.__head

    @head.setter
    def head(self, node):
        self.__head = node

    @head.deleter
    def head(self, node):
        del self.__head

    def addNode(self, element):
        # Each node should point to the next node
        new_node = Node(data=element, pointer=self.head)
        self.__head = new_node

    # Returns the deleted value, the most recent node added
    # AKA the Head
    def delNewestNode(self):
        node = self.head
        self.head = node.pointer
        return node.data

     # Delete First Node in list(the one pointing to Null)
    def delOldestNode(self):
        oldest_node = object
        node = self.__head
        prev_node = node
        while(node):
            if node.pointer is None:
                oldest_node = node
                if prev_node is not None:
                    prev_node.pointer = None
                return oldest_node.data
            prev_node = node
            node = node.pointer

    def length(self):
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
```

`Queue.py`

```python
#!/usr/bin/env python3
# 2019-1-18

from .LinkedList import LinkedList

# A Python implementetation of a 
# Queue using a linked list
class Queue:
    def __init__(self):
        self.__queue = LinkedList()

    def __str__(self):
        return str(self.__queue)
    
    def __repr__(self):
        return self.__queue.__repr__()

    def __del__(self):
        self.__queue = None

    @property
    def queue(self):
        return self.__queue
    
    def enqueue(self, element):
        self.__queue.addNode(element)

    def dequeue(self):
        return self.__queue.delOldestNode()
    
    # Returns the object at the top of the Queue without removing it.
    def peek(self):
        return self.__queue.head.data

    def length(self):
        return self.__queue.length()
```

`Stack.py`

```python
#!/usr/bin/env python3
# 2019-1-18

from .LinkedList import LinkedList

# A Python implementetation of a 
# Queue using a linked list
class Stack:
    def __init__(self):
        self.__stack = LinkedList()

    def __str__(self):
        return str(self.__stack)

    def __repr__(self):
        return self.__stack.__repr__()

    def __del__(self):
        self.__stack = None
        
    @property
    def stack(self):
        return self.__stack

    # Inserts an object at the top of the Stack.
    def push(self, element):
        self.__stack.addNode(element)

    # Removes and returns the object at the top of the Stack.
    def pop(self):
        return self.__stack.delNewestNode()

    # Returns the object at the top of the Stack without removing it.
    def peek(self):
        return self.__stack.head.data
	
    def clear(self):
        self.__stack = LinkedList()
    
    def length(self):
        return self.__stack.length()
```

`Palindrones.py`

```python
#!/usr/bin/env python3
# 2019-1-18
import time
import requests
from DataStructures.Queue import Queue
from DataStructures.Stack import Stack

class Palindrome:
    def __init__(self):
        self.magicitems = []
        self.palindrones = []

    def getMagicItems(self):
        try:
            file = open('./MagicItems.txt')
            items = file.read().splitlines()
            for item in items:
                self.magicitems.append(item)

        except:
            raise ValueError('File not found')

    
    def stackChars(self, item):
        s = Stack()
        for char in list(item):
            s.push(char)
        return s
        
    def queueChars(self, item):
        q = Queue()
        for char in list(item):
            q.enqueue(char)
        return q

    def checkForPalindrone(self):
        for item in self.magicitems:
            magic_item = item.lower()
            magic_item = ''.join(magic_item.split())
            stacked_item = self.stackChars(magic_item)
            queued_item = self.queueChars(magic_item)

            s_word = ''
            q_word = ''
            for i in range(len(magic_item)):
                s_word += stacked_item.pop()
                q_word += queued_item.dequeue()

            if s_word == q_word:
                self.palindrones.append(item)

if __name__ == "__main__":
   palindrome = Palindrome()
   palindrome.getMagicItems()
   palindrome.checkForPalindrone()
   print(palindrome.palindrones)
```

