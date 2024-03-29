#!/usr/bin/python3
"""
a script that lists all cities from the database hbtn_0e_4_usa
"""

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
    cursor.execute("SELECT cities.id, cities.name, states.name FROM cities\
                JOIN states ON cities.state_id = states.id\
                ORDER BY cities.id ASC")

    query = cursor.fetchall()

    for city in query:
        print(city)

    """close all cursors and databases"""
    cursor.close()
    db_connect.close()
