#!/usr/bin/env python

import sqlite3

s3conn = sqlite3.connect("../DATA/PRESIDENTS")
s3conn.row_factory = sqlite3.Row  # all cursors are Rows

NAME_QUERY = '''
    select lname, fname
    from presidents
    where num <= 5
'''

cur = s3conn.cursor() 

# select first name, last name from all presidents
cur.execute(NAME_QUERY)

for row in cur.fetchall():
    print(row['fname'], row['lname'])

print('-' * 60)
cur.execute(NAME_QUERY)

for row in cur.fetchall():
    print(row[0], row[1])
