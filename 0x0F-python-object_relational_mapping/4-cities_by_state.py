#!/usr/bin/python3
'''
    Lists all states from a given database with given name
    protect against sql injection
'''
import MySQLdb
from sys import argv
if __name__ == "__main__":
    connection = MySQLdb.connect(host="localhost", port=3306, charset="utf8",
                                 user=argv[1], passwd=argv[2], db=argv[3])
    cursor = connection.cursor()
    cursor.execute("SELECT cities.id, cities.name, states.name"
                   " FROM cities LEFT JOIN states"
                   " ON cities.state_id = states.id"
                   " ORDER BY cities.id ASC")
    rows = cursor.fetchall()

    for eachRow in rows:
        print(eachRow)

    cursor.close()
    connection.close()
