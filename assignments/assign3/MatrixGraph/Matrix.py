#!/usr/bin/env python3
# 2019-3-31

import re
import numpy as np


class Matrix:
    def __init__(self, commands):
        self.__commands = commands
        self.__matrix = []
        self.__size = 0
        self.buildMatrix()
        self.addConnections()
    
    def __str__(self):
        for row in self.__matrix:
            print(row)
        return ''

    ''' Properties '''
    @property
    def matrix(self):
        return self.__matrix

    ''' Methods '''
    def buildMatrix(self):
        for cmd in self.__commands:
            if re.match(r'add vertex .*', cmd):
               self.__size += 1

        if self.__size is not 0:
            [self.__matrix.append([0]*self.__size) for i in range(0,self.__size)]

    
    def addConnections(self):
        for cmd in self.__commands:
            if re.match(r'add edge .*', cmd):
                edge_vals = re.sub(r'add edge', '', cmd)
                values = edge_vals.split('-')
                self.__matrix[int(values[0].strip())-1][int(values[1].strip())-1] = 1
                self.__matrix[int(values[1].strip())-1][int(values[0].strip())-1] = 1
            