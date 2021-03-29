#!/usr/bin/python3
"""
Module that lists cities of the states
"""
import sys
import MySQLdb


if __name__ == "__main__":
    cnx = MySQLdb.connect(host="localhost", port=3306,
                          user=sys.argv[1], passwd=sys.argv[2],
                          db=sys.argv[3], charset="utf8")
    cur = cnx.cursor()
    cur.execute("SELECT cities.name FROM cities JOIN states ON \
                cities.state_id = states.id WHERE states.name \
                LIKE %s ORDER BY cities.id ASC", (sys.argv[4],))
    rows = cur.fetchall()
    print(", ".join(city[0] for city in rows))
    cur.close()
    cnx.close()
