#!/usr/bin/python3
""" a script that lists all states from the database hbtn_0e_0_usa"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    """
    Access the mysql  database and get the states
    from the database. connect to the mysql server
    """
    db_connect = MySQLdb.connect(
            host="localhost",
            user=argv[1],
            port=3306,
            passwd=argv[2],
            db=argv[3])
    """ Create a cursor object to execute queries"""
    cursor = db_connect.cursor()

    """ Execute the query to retrieve states"""
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    """ Fetch all the rows"""
    states = cursor.fetchall()

    """ Display results"""
    for state in states:
        print(state)

    """ Close the cursor and database connection"""
    cursor.close()
    db_connect.close()
