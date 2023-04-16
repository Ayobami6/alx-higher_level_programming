#!/usr/bin/python3
""" Select all columns from states table in hbtn database where
name is the last arg passed from the commandline and preventing
sql injection attack and filtering based on the 5 arg passed from
the commandline
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
        """SELECT c.name FROM cities as c INNER JOIN\
         states as s ON s.id=c.state_id \
         WHERE s.name=%s""", (argv[4],))
    # getting all query result
    rows = cursor.fetchall()
    new_list = []
    for row in rows:
        new_list.append(row[0])
    print(*new_list, sep=", ")
    # close cursor environment
    cursor.close()
    # close the database
    db.close()
