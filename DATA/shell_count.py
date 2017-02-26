#!/usr/bin/env python
#Created by jinshiwu on 2/15/17.


shell_dict = {}
with open('../DATA/passwd', 'r') as pwd_in:
    for line in pwd_in:
        (name1, name2, name3, name4, name5, name6, shell) = line[:-1].split(':')
        if shell == '':
            shell = 'None'
        else:
            shell_dict[shell] = shell_dict.get(shell, 0) +1

for key, item in sorted(shell_dict.items()):
    print("{0:20s} \t {1:2d}".format(key, item))


set1={'1','2','3','4'}
set2={'4','5','6','7'}
set3=set1 ^ (set2)
print(set3)