#!/usr/bin/python3
'''
    Lists all states from a given database starting with N
'''
import MySQLdb
from sys import argv

if __name__ == "__main__":
    connection = MySQLdb.connect(host="localhost", port=3306, charset="utf8",
                                 user=argv[1], passwd=argv[2], db=argv[3])
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM states WHERE name ='" + argv[4] + "' ORDER BY states.id ASC")
    rows = cursor.fetchall()

    for eachRow in rows:
        if eachRow[1] == argv[4]:
            print(eachRow)

    cursor.close()
    connection.close()
