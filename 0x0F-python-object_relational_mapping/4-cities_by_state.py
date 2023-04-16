#!/usr/bin/python3
""" Select all columns from states table in hbtn database where
name is the last arg passed from the commandline and preventing
sql injection attack
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
        "SELECT cities.id, cities.name, states.name FROM cities \
        INNER JOIN states ON states.id=cities.state_id")
    # getting all query result
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    # close cursor environment
    cursor.close()
    # close the database
    db.close()
