#!/usr/bin/env python

import sqlite3

with sqlite3.connect("../DATA/PRESIDENTS") as s3conn:

    s3cursor = s3conn.cursor()

    # select first name, last name from all presidents
    s3cursor.execute('''
        select lname, fname
        from presidents
        where lname like 'J%'
    ''')

    for row in s3cursor.fetchall():
        print(row)
    print('-' * 60)

    # cursor not needed...
    president_count = s3conn.execute(
        'select count(*) from presidents'
    ).fetchone()
    print(president_count[0])
    print('-' * 60)

    # fetchall not needed...
    for last_name, first_name in s3conn.execute(
        """
        select lname, fname
        from presidents
        where lname like "C%"
        """
    ):
        print(first_name, last_name)
