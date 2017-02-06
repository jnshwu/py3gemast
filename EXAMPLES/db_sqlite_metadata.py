#!/usr/bin/env python
"""
    Provide metadata (tables and column names) for a Sqlite3 database
"""

import sqlite3

TABLE_QUERY = '''
    select name
    from sqlite_master
    order by name
'''

def main(s3database):
    """
        Program entry point

        PARAMS:
        s3database: name of Sqlite3 database file
    """
    # column_format = '\t{:15s} {:12s} {:1d} {:10.10s}'
    column_format = '\t{:15s} {:15} {:1d} {:10s}'
    s3cursor = connect_to_dbserver(s3database)
    tables = get_all_tables_from_database(s3cursor)
    for table in tables:
        print(table)
        columns = get_columns_for_table(s3cursor, table)
        for col_name, col_type, col_nullable, col_default in columns:
            print(column_format.format(col_name, col_type, col_nullable, str(col_default)))
        print('-' * 60)

def connect_to_dbserver(database_file):
    """
        Connect to specified Sqlite3 database

        PARAMS:
        database_file: name of Sqlite3 database file to query
    """
    with sqlite3.connect(database_file) as s3conn:
        return s3conn.cursor()


def get_all_tables_from_database(mycursor):
    """
        Get list of tables in database

        PARAMS:
        mycursor: open Sqlite3 database cursor

        :rtype : list of table names
    """

    mycursor.execute(TABLE_QUERY)

    return [row[0] for row in mycursor.fetchall() if not row[0].startswith('sqlite')]


def get_columns_for_table(mycursor, table_name):
    """
        Get list of columns and metadata for specified table

        PARAMS:
        mycursor: open Sqlite3 database cursor
        table_name: table for which to return columns

        CAUTION: do not pass unverified information to this function;
        it is not checked for SQL injection issues

        :rtype : list of lists, each with name, type, nullable flag, and default value
    """

    mycursor.execute('pragma table_info({})'.format(table_name))
    return [row[1:-1] for row in mycursor.fetchall()]  # 1st column is ordinal; last is PK flag


if __name__ == '__main__':
    main("../DATA/PRESIDENTS")
