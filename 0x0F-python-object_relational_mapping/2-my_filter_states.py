#!/usr/bin/python3
"""
Module that all values in the states table
where name matches an argument
"""
import sys
import MySQLdb

if __name__ == "__main__":
    database = MySQLdb.connect(host="localhost", port=3306,
                               user=sys.argv[1], passwd=sys.argv[2],
                               db=sys.argv[3], charset="utf8")
    cur = database.cursor()
    sta = sys.argv[4]
    cur.execute("SELECT * FROM states WHERE name= '{:s}' ORDER BY id ASC"
                .format(sta))
    row = cur.fetchall()
    for i in row:
        if i[1] == sta:
            print(i)
    cur.close()
    database.close()
