#!/usr/bin/env python3
# 2019-5-5

class Knapsack:
    def __init__(self, capacity):
        self.__capacity = capacity

    def __str__(self):
        return f'capacity={self.capacity};'
    
    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, capacity):
        self.__capacity = capacity