#!/usr/bin/env python3
'''
    Lists all states from a given database
'''
import MySQLdb
from sys import argv

if __name__ == "__main__":
    connection = MySQLdb.connect(host="localhost", port=3306, charset="utf8",
                                 user=argv[1], passwd=argv[2], db=argv[3])
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM states WHERE name REGEXP '^N'")
    rows = cursor.fetchall()

    for eachRow in rows:
        print(eachRow)

    cursor.close()
    connection.close()
