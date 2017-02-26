#!/usr/bin/env python

count_of = {}
with open("../DATA/passwd") as pw:
    for line in pw:
        (user,epw,uid,gid,comment,home,shell) = line[:-1].split(":")
        if shell == "":
            shell = "NONE"
        count_of[shell] = count_of.get(shell,0) + 1

for shell,count in count_of.items():
    print("{0:5d} {1}".format(count,shell))

fruit_set=set()

with open('../DATA/fruit1.txt', 'r') as fruit1:
    print('fruit1 number is {0}'.format(len(fruit1.readline())))
    for line in fruit1:
        fruit_set.add(line[:-1].strip())

with open('../DATA/fruit2.txt', 'r') as fruit2:
    print('fruit2 number is {0}'.format(len((fruit2.readline()))))
    for line in fruit2:
        fruit_set.add(line[:-1].strip())

print(fruit_set)
print('total fruit number is {0}'.format(len(fruit_set)))