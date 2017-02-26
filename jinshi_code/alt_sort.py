#!/usr/bin/env python
#Created by jinshiwu on 2/23/17.

a=[]
b=[]

with open('../DATA/alt.txt', 'r') as alt_in:
    for line in alt_in:
        if line.strip().startswith('a'):
            a.append(line)
        elif line.strip().startswith('b'):
            b.append(line)

print(''.join(sorted(a)))
print('*'*45)
print(''.join(sorted(b, reverse=True)))


student = {}
with open('../DATA/testscores.dat') as score_in:
    for line in score_in:
        (name, score) = line[:-1].split(':')
        student[name] = score

for name, score in sorted(student.items(), reverse = True, key = lambda e: e[1]):
    print(name, score)


president = []
with open('../DATA/presidents.txt') as president_in:
    for line in president_in:
        president.append(line[:-1].split(':'))

print(sorted(president, key = lambda e: int(e[0])))

for line in sorted(president, key = lambda e:(e[1], e[2])):
    print('{0} {1}'.format(line[2], line[1]))


