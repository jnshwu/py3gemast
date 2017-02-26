#!/usr/bin/env python
#Created by jinshiwu on 2/13/17.

knights_info = {}
with open('../DATA/knights.txt') as knights_in:
    for line in knights_in:
        (name, position, color, quote, etc) = line[:-1].split(':')
        knights_info[name] = (position,color,quote,etc)

for name, info in sorted(knights_info.items()):
    print("{0:10s}\t".format(name), info)