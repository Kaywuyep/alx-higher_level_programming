#!/usr/bin/python3
"""a script that takes in arguments and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument.
But this time, the script is safe from MySQL injections!"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    """
    connect to MySQLdb server
    """
    db_connect = MySQLdb.connect(
            host="localhost",
            user=argv[1],
            port=3306,
            passwd=argv[2],
            db=argv[3])

    cursor = db_connect.cursor()
    cursor.execute("SELECT * FROM states WHERE name=%s", (argv[4],))
    """ fetches all the rows of a query result"""
    query = cursor.fetchall()

    for state in query:
        print(state)

    """ Close all cursors and databases"""
    cursor.close()
    db_connect.close()
