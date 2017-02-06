#!/usr/bin/env python
# (c) 2016 John Strickler
#
import sqlite3

INSERT_SQL = """
INSERT INTO python_books
(author, title, publisher, pub_year)
VALUES (?, ?, ?, ?);
"""

conn = sqlite3.connect("../DATA/PYTHON_BOOKS")

cur = conn.cursor()

with open('../DATA/python_books.tsv') as books_in:
    for row in books_in:
        values = row.rstrip('\n\r').split('\t')
        cur.execute(INSERT_SQL, values)

conn.commit()
