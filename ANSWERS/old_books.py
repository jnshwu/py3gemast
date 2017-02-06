#!/usr/bin/env python
# (c) 2016 John Strickler
#
import sqlite3

with sqlite3.connect('../DATA/PYTHON_BOOKS') as conn:
    cur = conn.cursor()
    for author, title, year in cur.execute("""
        select author, title, pub_year
        from python_books
        where pub_year < 2010
    """
    ):
        print(author, title, year)
