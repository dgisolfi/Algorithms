#!/usr/bin/env python3
# 2019-5-3

class Edge:
    def __init__(self, source, target, weight):
        self.__source = source
        self.__target = target
        self.__weight = weight

    def __str__(self):
        return f'{self.source}=>{self.target} weight={int(self.weight)}'
    
    @property
    def source(self):
        return self.__source
    
    @source.setter
    def source(self, source):
        self.__source = source
    
    @property
    def target(self):
        return self.__target
    
    @target.setter
    def target(self, target):
        self.__target = target

    @property
    def weight(self):
        return self.__weight
    
    @weight.setter
    def weight(self, weight):
        self.__weight = weight