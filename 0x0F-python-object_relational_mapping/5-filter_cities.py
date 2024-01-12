#!/usr/bin/python3
"""
a script that takes in the name of a state as an argument
lists all cities of that state, using the database hbtn_0e_4_usa
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
    cursor.execute("SELECT cities.name FROM cities\
            JOIN states ON cities.state_id = states.id\
            WHERE  states.name=%s ORDER BY cities.id ASC", (argv[4], ))

    query = cursor.fetchall()

    cities = []
    # Printing the cities one in one
    for city in query:
        cities.append(city[0])
    print(", ".join(cities))  # Printing DATABASE of states name

    """close all cursors and databases"""
    cursor.close()
    db_connect.close()
