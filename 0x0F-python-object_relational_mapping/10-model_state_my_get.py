#!/usr/bin/python3
"""script that prints the first State object from the database
hbtn_0e_6_usa"""
from sqlalchemy import (create_engine)
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sys import argv


if __name__ == "__main__":
    """Connect to the database"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1],
        argv[2],
        argv[3]),
        pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).filter(State.name.like(
        '%s' % (argv[4], ))).first()
    if states is None:
        print("Not found")
    else:
        print(states.id)
    session.close()
