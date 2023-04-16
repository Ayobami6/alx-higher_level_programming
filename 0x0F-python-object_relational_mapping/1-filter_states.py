#!/usr/bin/python3
""" Select all columns from states table in hbtn database where
first letter in the name starts with N order by id
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    # connect to database with the args passed from the commandline
    db = MySQLdb.connect(
        host="localhost", user=argv[1], passwd=argv[2], db=argv[3], port=3306)
    # establishing cursor
    cursor = db.cursor()
    # executing the query from cursor environment
    cursor.execute(
        """SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id""")
    # getting all query result
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    # close cursor environment
    cursor.close()
    # close the database
    db.close()
