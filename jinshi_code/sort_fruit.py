#!/usr/bin/env python
#Created by jinshiwu on 2/22/17.

fruit = ["pomegranate","cherry","apricot","date","Apple","lemon","Kiwi",
         "ORANGE","lime","Watermelon","guava","papaya","FIG","pear","banana",
         "Tamarind","persimmon","elderberry","peach","BLUEberry","lychee",
         "grape" ]
sorted_fruit = sorted(fruit)
print(' '.join(sorted_fruit))

print(sorted(fruit, key=len))


computer_guys = [
    ('Mark', 'Zuckerberg', 'Facebook'),
    ('Guido', 'Van Rossum', 'Python'),
    ('Larry', 'Wall', 'Perl'),
    ('Bill', 'Joy', 'Sun'),
    ('Bill', 'Gates', 'Microsoft'),
    ('Steve', 'Case', 'AOL'),
    ('Larry', 'Ellison', 'Oracle'),
    ('Steve', 'Jobs', 'Apple'),
    ('Dennis', 'Ritchie', 'Unix'),
]
#
# for firstName, lastName, company in sorted(computer_guys):
#     print(firstName, lastName, company)

for firstName, lastName, comapny in sorted(computer_guys, key = lambda e: e[1]):
    print(firstName, lastName, comapny)