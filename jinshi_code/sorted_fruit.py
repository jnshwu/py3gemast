#!/usr/bin/env python
#Created by jinshiwu on 2/22/17.

with open('../DATA/fruit.txt', 'r') as fruit_in:
    fruits_lines = fruit_in.readlines()

print(''.join(sorted(fruits_lines)))



print('*'*60)

print(''.join(sorted(fruits_lines, key=lambda e: len(e))))

print(''.join(sorted(fruits_lines, key = lambda e: (e.lower(), len(e)))))

print('*'*60)
print(''.join(sorted(fruits_lines, key = lambda a: (a[0].lower()))))