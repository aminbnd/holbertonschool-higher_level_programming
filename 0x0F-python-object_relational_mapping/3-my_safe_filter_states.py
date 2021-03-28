#!/usr/bin/python3
"""
Module that displays all values in the states
table where name matches the argument
safe from SQL injection
"""


from sys import argv
import MySQLdb


def main():
    cnx = MySQLdb.connect(host="localhost", port=3306,
                          user=argv[1], passwd=argv[2],
                          db=argv[3], charset="utf8")
    cur = cnx.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE '{:s}' ORDER BY id ASC"
                .format(argv[4]))
    rows = cur.fetchall()
    for i in rows:
        if i[1] == argv[4]:
            print(i)
    cur.close()
    cnx.close()

if __name__ == "__main__":
    main()
