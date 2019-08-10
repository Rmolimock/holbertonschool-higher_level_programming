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
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cursor.fetchall()

    names = {}
    for eachRow in rows:
        names[eachRow[1]] = eachRow[1]

    if argv[4] in names:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM states WHERE BINARY name ='{}' "
                       .format(argv[4]) + "ORDER BY id ASC")
        rows = cursor.fetchall()
        for eachRow in rows:
            print(eachRow)
        cursor.close()
        connection.close()
