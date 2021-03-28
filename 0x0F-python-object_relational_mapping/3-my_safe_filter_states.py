#!/usr/bin/python3
"""
Module that displays all values in the states
table where name matches the argument
safe from SQL injection
"""


import sys
import MySQLdb


if __name__ == "__main__":
    cnx = MySQLdb.connect(host="localhost", port=3306,
                          user=sys.argv[1], passwd=sys.argv[2],
                          db=sys.argv[3], charset="utf8")
    cur = cnx.cursor()
    sta = sys.argv[4]
    cur.execute("SELECT * FROM states WHERE name LIKE %s ORDER BY id ASC"
                .format(sta))
    rows = cur.fetchall()
    for i in rows:
        if i[1] == sys.argv[4]:
            print(i)
    cur.close()
    cnx.close()
