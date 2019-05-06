#!/usr/bin/env python3
# 2019-5-5

class Knapsack:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__value = 0
        self.__cur_quantity = 0
        

    def __str__(self):
        return f'capacity={self.capacity};'
    
    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, capacity):
        self.__capacity = capacity

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value

    @property
    def cur_quantity(self):
        return self.__cur_quantity

    @cur_quantity.setter
    def cur_quantity(self, cur_quantity):
        self.__cur_quantity = cur_quantity