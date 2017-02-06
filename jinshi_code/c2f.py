#!/usr/bin/env python
#Created by jinshiwu on 2/4/17.

import sys

def f2c(f):
    c = (float(f) - 32) * 5 / 9
    return "{0:6.2f}".format(c)

if len(sys.argv) > 1:
    for tempa in sys.argv[1:]:
        print(tempa, f2c(tempa))

print("100 {0: 6.2f}".format(f2c(100)))
print("0 {0: 6.2f}".format(f2c(0)))
print("37 {0: 6.2f}".format(f2c(37)))
print("-40 {0: 6.2f}".format(f2c(-40)))




while True:
    temp= str(input("please input temp"))
    if temp.lower() == 'q':
        print("quit")
        break
    elif str == '':
        continue
    print(temp, 'in C is' , f2c(temp))