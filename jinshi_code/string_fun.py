#!/usr/bin/env python
#Created by jinshiwu on 2/4/17.

import sys
#
# Print out the name as-is
# 2. Print the name in upper case
# 3. Print the name in title case
# 4. Print the number of occurrences of 'j' (case-insensitive)
# 5. Print the length of the name
# 6. Print the position (offset) of "jacob" in the string( case-insensitive)

names = "john jacob jingleheimer smith"

print("names ", names)
print("names in UPPER ", names.upper())
print("names in title case", names.title())
print("names counting j ", names.lower().count('j'))
for aName in names.split():
    print(aName, ' length', len(aName))

print("jacob offset ", names.index('jacob'))