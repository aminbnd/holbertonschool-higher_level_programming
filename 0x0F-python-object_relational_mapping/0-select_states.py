#!/usr/bin/python3
"""
Module that lists states
"""
import sys
import MySQLdb


def main():
    con = MySQLdb.connect(
                        host="localhost",
                        port=3306,
                        user=sys.argv[1],
                        passwd=sys.argv[2],
                        db=sys.argv[3],
                        charset="utf8"
                            )
    cur = con.cursor()
    query = "SELECT id,name FROM states ORDER BY id ASC"
    cur.execute(query)
    row = cur.fetchall()
    for i in row:
        print(i)
    cur.close()
    con.close()
if __name__ == "__main__":
    main()
