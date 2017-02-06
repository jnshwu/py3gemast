#!/usr/bin/env python
from datetime import date
import sqlite3

s3conn = sqlite3.connect("../DATA/PRESIDENTS")

INSERT = '''
    insert into presidents
    (num, fname, lname, dstart, dend, birthplace,
    birthstate, dbirth, ddeath, party)
    values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
'''

cur = s3conn.cursor() 

data = [45, 'Gates', 'Bill', date(2017, 1, 20), date(2021, 1, 20),
    'Seattle', 'Washington', date(1955, 10, 28), None,
    'Independent']

cur.execute(INSERT, data)

last_row_id = cur.lastrowid

print("Last row ID is", last_row_id)
