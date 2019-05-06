#!/usr/bin/env python3
# 2019-3-29

import re
import sys

class Parser:
    def __init__(self, filename):
        self.filename = filename
        self.__commands = []
        self.__graph_count = 0
        self.__graph_commands = []
        self.parse()
        
    ''' Properties '''
    @property
    def commands(self):
        return self.__commands

    @property
    def graph_count(self):
        return self.__graph_count

    @property
    def graph_commands(self):
        return self.__graph_commands


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
        # seperate the graphs 
        graph = []
        for cmd in self.commands:
            if re.match(r'new graph', cmd):
                self.__graph_count += 1
                if len(graph) is not 0:
                    self.__graph_commands.append(graph)
                    graph = []
            elif cmd is '':
                continue
            else:
                graph.append(cmd)
                
        if len(graph) is not 0:
            self.__graph_commands.append(graph)