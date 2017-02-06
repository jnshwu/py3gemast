#!/usr/bin/python3
import sqlite3

DATA = [
    ["Expert Python Programming ", "Tarek Ziadé ", "Packt Publishing", "2008"],
    ["Learning Python, 5th Ed.", "Mark Lutz, David Asher ", "O'Reilly & Assoc.", "2013"],
    ["Matplotlib for Python Developers", "Sandro Tosi ", "Packt Publishing", "2009"],
    ["Numpy Beginner's Guide ", "Ivan Idris ", "Packt Publishing", "2015"],
    ["Numpy Cookbook, 2nd Ed. ", "Ivan Idris ", "Packt Publishing", "2015"],
    ["Programming Python, 4th Ed.", "Mark Lutz ", "O'Reilly & Assoc.", "2011"],
    ["Python Cookbook, 3rd Ed.", "David Beazley, Brian K. Jones", "O'Reilly & Assoc.", "2013"],
    ["Python Essential Reference, 4th Ed.", "David M. Beazley", "Addison-Wesley Professional", "2009"],
    ["Python in a Nutshell, 3rd Ed.", "Alex Martelli ", "O'Reilly & Assoc.", "2016"],
    ["Python Programming on Win32 ", "Mark Hammond, Andy Robinson ", "O'Reilly & Assoc.", "2000"],
]

TABLE_CHECK_SQL = """
    select count(*)
    from sqlite_master
    where
        type = 'table'
        and
        name = 'python_books'
"""

CREATE_TABLE_SQL = """
create table python_books (
    id integer primary key,
    author varchar(256),
    title varchar(128),
    publisher varchar(64),
    pub_year int
);
"""

INSERT_SQL = """
INSERT INTO python_books
(id, author, title, publisher, pub_year)
VALUES (null, ?, ?, ?, ?);
"""


myconn = sqlite3.connect("../DATA/PYTHON_BOOKS")

cur = myconn.cursor()

cur.execute(TABLE_CHECK_SQL)
result = cur.fetchone()
if result[0] > 0:
    cur.execute("drop table python_books")

cur.execute(CREATE_TABLE_SQL)

cur.executemany(INSERT_SQL, DATA)

myconn.commit()
