#!/usr/bin/env python3
# 2019-5-5

import re
import sys
from .spice import Spice
from .knapsack import Knapsack
from .LinkedList import LinkedList

class Parser:
    def __init__(self, filename):
        self.filename = filename
        self.__commands = []
        self.__knapsacks = []
        self.__spices = LinkedList()
        self.parse()
        
    ''' Properties '''
    @property
    def commands(self):
        return self.__commands

    @property
    def knapsacks(self):
        return self.__knapsacks
        
    @knapsacks.setter
    def knapsacks(self, knapsacks):
        self.__knapsacks = knapsacks

    @property
    def spices(self):
        return self.__spices

    @spices.setter
    def spices(self, spices):
        self.__spices = spices

    ''' Methods '''
    def getCmds(self, filename):
        try:
            file = open(filename, 'r')
            commands = file.readlines()
            file.close()
            return commands
        except Exception as e:
            print(f'Error: {e}')
    
    def removeExtraSyntax(self):
        self.__commands = [re.sub(r'\n', '', line) for line in self.__commands]
        self.__commands = [re.sub(r'^--.*$', '', line) for line in self.__commands]
        
        
    def parse(self):
        # Get all commands from the file
        self.__commands = self.getCmds(self.filename)
        # Remove the comments and line breaks from the commands
        self.removeExtraSyntax()

        # parse all spices and knapsacks
        for cmd in self.commands:
            if re.match(r'^spice.*', cmd):
                cmd = cmd.replace('spice', '').replace(';', '')
                attributes = cmd.split()

                name = attributes[0].split('=')[1]
                price = attributes[1].split('=')[1]
                quantity = attributes[2].split('=')[1]
                
                self.spices.append(Spice(name, price, quantity))
            
            if re.match(r'^knapsack.*', cmd):
                cmd = cmd.replace('knapsack', '').replace(';', '')
                capacity = cmd.split('=')[1]
                self.knapsacks.append(Knapsack(capacity))
