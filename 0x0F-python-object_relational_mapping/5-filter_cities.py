#!/usr/bin/python3
'''
    Lists all cities associated with given state
'''
import MySQLdb
from sys import argv
if __name__ == "__main__":
    connection = MySQLdb.connect(host="localhost", port=3306, charset="utf8",
                                 user=argv[1], passwd=argv[2], db=argv[3])
    cursor = connection.cursor()
    selection = "SELECT cities.name FROM cities " +\
                "JOIN states ON cities.state_id = states.id " +\
                "WHERE states.name = %s ORDER BY cities.id ASC"
    cursor.execute(selection, (argv[4],))
    rows = cursor.fetchall()

    ret = ""
    flag = False
    for eachRow in rows:
        ret += ', ' if flag else ''
        flag = True
        ret += eachRow[0]
    print(ret)
    cursor.close()
    connection.close()
