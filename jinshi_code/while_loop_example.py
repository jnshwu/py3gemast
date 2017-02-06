#!/usr/bin/env python
#Created by jinshiwu on 2/4/17.

while True:
    name = str(input("Enter a name (or q to quit): "))
    if name.lower() == 'q':
        print("goodbye!")
        break
    if name == '':
        continue
    print("welcome,", name)