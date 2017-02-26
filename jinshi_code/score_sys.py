#!/usr/bin/env python
#Created by jinshiwu on 2/13/17.

score_record = dict()
total = 0

def grade_score(score):
    if (int(score) <= 100 and int(score) > 95):
        grade = 'A'
    elif (int(score) <= 95 and int(score) > 85):
        grade = 'B'
    elif (int(score) <=85 and int(score) >74):
        grade = 'C'
    elif (int(score) <= 74 and int(score) > 65):
        grade = 'D'
    else:
        grade = 'F'
    return grade


with open('../DATA/testscores.dat', 'r') as test_score_in:
    for line in test_score_in:
        (name, score) = line[:-1].split(':')
        grade = grade_score(score)
        score_record[name] = (score, grade)

for name, item in sorted(score_record.items()):
    total = total + int(item[0])
    print("{0:<20s}\t {1} \t {2}".format(name, item[0], item[1]))

print("total student is {0}, average score is {1:.2f}".format(len(score_record), total/(len(score_record))))