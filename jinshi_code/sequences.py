#!/usr/bin/env python
#Created by jinshiwu on 2/6/17.

ctemps = [ -40.0, 0.0, 37.0, 75.0, 100.0, -1 ]

fruits = [
    '    MANGO', 'Apple', '   peach   ', 'PLUM   ', '  Apricot',
    'BaNaNa', 'Persimmon   '
]

computer_people = [
    ('Bill', 'Gates', 'Windows'),
    ('Bill', 'Joy', 'Sun Microsystems'),
    ('Brian', 'Kernighan', 'Unix'),
    ('Dennis', 'Ritchie', 'Unix'),
    ('Ken', 'Thompson', 'Unix'),
    ('Guido', 'van Rossum', 'Python'),
    ('Larry', 'Wall', 'Perl'),
    ('Matz','Matsumoto', 'Ruby'),
    ('John', 'Osterhout', 'TCL'),
    ('Linus', 'Torvalds', 'Linux'),
]


for c in ctemps:
    print(float(c) * 9 / 5 + 32)

for i, c in enumerate(fruits, 1):
    print(i, c.strip())


clean_fruit = []
for c in fruits:
    clean_fruit.append(c.lower().strip())

print(clean_fruit)


for c in computer_people:
    print(c[1])