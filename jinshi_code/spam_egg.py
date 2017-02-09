#!/usr/bin/env python
#Created by jinshiwu on 2/7/17.

with open('../DATA/spam.txt', 'r') as spam_in:
    for line in spam_in:
        print(line, end='')

with open("../DATA/eggs.txt") as eg:
    eggs = eg.readlines()
print("\n\n** About Eggs **")
print(eggs[0], end='')
print(eggs[1], end='')
print(eggs[2], end='')