#!/usr/bin/python3
"""
a script that lists all states with a name starting with
N (upper N) from the database hbtn_0e_0_usa
"""

from sys import argv
import MySQLdb

if __name__ == "__main__":
    """
    Access database and connect to mysql server
    """
    db_connect = MySQLdb.connect(
            host="localhost",
            user=argv[1],
            port=3306,
            passwd=argv[2],
            db=argv[3])

    cursor = db_connect.cursor()

    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    """ Fetch all the rows"""
    states = cursor.fetchall()

    for state in states:
        if state[1][0] == 'N':
            print(state)

    cursor.close()
    db_connect.close()
