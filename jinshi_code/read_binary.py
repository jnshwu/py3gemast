#!/usr/bin/env python
#Created by jinshiwu on 2/7/17.

with open('../DATA/parrot.txt', 'rb') as parrot_in:
    while (True):
        trunk = parrot_in.read(100).decode()
        if (trunk == ''):
            break
        print(trunk)
