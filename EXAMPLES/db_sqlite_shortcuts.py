#!/usr/bin/env python

import sqlite3
rows = sqlite3.connect(
    '../DATA/PRESIDENTS'
).execute(
    """
    select fname, lname from presidents
    where lname like 'J%'
    """
).fetchall()
print(rows)
