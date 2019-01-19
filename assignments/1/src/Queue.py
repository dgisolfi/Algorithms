#!/usr/bin/env python3
# 2019-

# A Python implementetation of a 
# singly linked list
class Queue:
    def __init__(self, *args, **kwargs):
        self.q = []

    def __str__(self):
        return str(self.q)
    
    def __repr__(self):
        return f'{self.__class__}({self.q})'

    def __del__(self):
        self.q = None

    def enqueue(self, element):
        self.q.append(element)

    def dequeue(self):
        self.q.pop(0)

    def length(self):
        return len(self.q)

    