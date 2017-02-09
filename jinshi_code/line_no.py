#!/usr/bin/env python
#Created by jinshiwu on 2/8/17.

import sys


def print_lines(name):
    with open(name, 'r') as file_in:
        for i,line in enumerate(file_in,1):
            print (i,line, end='')


if len(sys.argv) > 1:
    for name in sys.argv[1:]:
        print_lines(name)
else:
    name = input("please input file name")
    print_lines(name)