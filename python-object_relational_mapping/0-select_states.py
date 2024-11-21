#!/usr/bin/python3
""" Module to list all states from a database """
import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306
    )
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states")
    for state in cursor.fetchall():
        print(state)
