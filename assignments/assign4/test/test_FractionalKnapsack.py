#!/usr/bin/env python3
# 2019-5-5

import sys
sys.path.append('..')
from assign4.FractionalKnapsack.parser import Parser

parser = Parser('./test/spice.txt')

for cmds in parser.commands:
    pass