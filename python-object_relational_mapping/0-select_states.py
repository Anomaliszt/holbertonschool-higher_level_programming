#!/usr/bin/python3
"""
lists all states from the database hbtn_0e_0_usa
take 3 arguments
"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3],
                         port=3306)
    c = db.cursor()
    c.execute("SELECT * FROM states ORDER BY states.id ASC")
    [print(state) for state in c.fetchall()]
    c.close()
    db.close()