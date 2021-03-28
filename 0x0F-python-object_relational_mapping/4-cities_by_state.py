#!/usr/bin/python3
"""
Module that lists all cities from
hbtn_0e_4_usa database
"""

import sys
import MySQLdb

if __name__ == "__main__":
    cnx = MySQLdb.connect(host="localhost", port=3306,
                          user=sys.argv[1], passwd=sys.argv[2],
                          db=sys.argv[3], charset="utf8")
    cur = cnx.cursor()
    query = """SELECT cities.id, cities.name, states.name
                FROM cities INNER JOIN states ON cities.state_id=states.id
                ORDER BY cities.id ASC"""
    cur.execute(query)
    row = cur.fetchall()
    for i in row:
        print(i)
    cur.close()
    cnx.close()
