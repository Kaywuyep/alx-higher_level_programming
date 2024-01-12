#!/usr/bin/python3
"""script that prints the first State object from the database
hbtn_0e_6_usa"""
from sqlalchemy import (create_engine)
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sys import argv


if __name__ == "__main__":
    """Connect to the engine"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1],
        argv[2],
        argv[3]),
        pool_pre_ping=True)
    # create a table
    Base.metadata.create_all(engine)
    # create a session
    Session = sessionmaker(bind=engine)
    session = Session()
    # query the first state object
    firstState = session.query(State).first()
    # print out the results
    if firstState is None:
        print("Nothing")
    else:
        print("{}: {}".format(firstState.id, firstState.name))
    # close session
    session.close()
