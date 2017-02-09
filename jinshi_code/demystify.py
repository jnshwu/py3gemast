#!/usr/bin/env python
#Created by jinshiwu on 2/8/17.

with open('../DATA/mystery', 'br') as mystery_in:
    all_bytes = mystery_in.read()

print(all_bytes[::2].decode())

with open('../DATA/parrot.txt', 'a') as parrot_in:
    parrot_in.write("The preceding joke (c) 1937 by Laffs-a-Minute, Inc.")