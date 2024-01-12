#!/usr/bin/python3
"""
a script that takes in an argument and displays all values in
the states table of hbtn_0e_0_usa where name matches the argument.
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    """
    access the database and connect to mysql
    """
    db_connect = MySQLdb.connect(
            host="localhost",
            user=argv[1],
            port=3306,
            passwd=argv[2],
            db=argv[3])

    cursor = db_connect.cursor()
    """ Get the search term from command-line arguments
    The execute function requires one parameter, the query."""
    cursor.execute("SELECT * FROM states\
        WHERE BINARY name = '{}'\
            ORDER BY id ASC".format(argv[4]))
    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    db_connect.close()
