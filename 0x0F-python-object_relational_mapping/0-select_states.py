#!/usr/bin/env python3
import MySQLdb
from sys import argv


if __name__ == '__main__':
    conn = MySQLdb.connect(host="localhost", port=3306, charset="utf8",
                           user=argv[1], passwd=argv[2], db=argv[3])
    c = conn.cursor()
    c.execute("SELECT * FROM states ORDER BY states.id ASC")
    rows = c.fetchall()
    for each in rows:
        print(each)
