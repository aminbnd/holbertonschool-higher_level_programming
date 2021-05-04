#!/usr/bin/python3
"""
Module that lists states with names starts with N
from the database hbtn_0e_0_usa
"""

import sys
import MySQLdb

if __name__ == "__main__":
    database = MySQLdb.connect(host="localhost", port=3306,
                               user=sys.argv[1], passwd=sys.argv[2],
                               db=sys.argv[3],
                               charset="utf8")
    cur = database.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    row = cur.fetchall()
    for i in row:
        if i[1][0] == 'N':
            print(i)
    cur.close()
    database.close()
