#!/usr/bin/env python
#Created by jinshiwu on 2/3/17.

import unicodedata

u = chr(233) + chr(0x0bf2) + chr(3972) + chr(6000) + chr(13231)

for i, c in enumerate(u):
    print(i, '%04x' % ord(c), unicodedata.category(c), end=" ")
    print(unicodedata.name(c))

# Get numeric value of second character
print(unicodedata.numeric(u[1]))

print("hello world".count('hello'))


print('we spent \u20ac1.23M for an original C\u00e9zanne')
print('26\u00B0')
print('26\N{DEGREE SIGN}')
print('26\u00B0')
print(r'26\u00B0\n')
print(r'26\N{DEGREE SIGN}')


print('\x57')
print('\x58')
print('\x59')