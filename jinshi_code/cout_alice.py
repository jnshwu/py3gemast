#!/usr/bin/env python
#Created by jinshiwu on 2/8/17.

import sys

def count_word(name, str):
    num = 0
    with open(name) as file_in:
        for line in file_in:
            if line.find(str) >=0:
                num += 1
    return num

if len(sys.argv) == 3:
    name = sys.argv[1]
    str = sys.argv[2]
    print("file {0}, word  {1} appears {2}".format(name, str, count_word(name, str)))
