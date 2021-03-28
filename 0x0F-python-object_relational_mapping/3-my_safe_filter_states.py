#!/usr/bin/python3
"""
Module that displays all values in the states
table where name matches the argument
safe from SQL injection
"""


from sys import argv
import MySQLdb


if __name__ == "__main__":
    cnx = MySQLdb.connect(host="localhost", port=3306,
                          user=argv[1], passwd=argv[2],
                          db=argv[3], charset="utf8")
    cur = cnx.cursor()
    sta = argv[4]
    cur.execute("SELECT * FROM states WHERE name LIKE '{:s}' ORDER BY id ASC"
                .format(sta))
    rows = cur.fetchall()
    for i in rows:
        if i[1] == argv[4]:
            print(i)
    cur.close()
    cnx.close()
