#!/usr/bin/python3
"""script that prints the first State object from the database
hbtn_0e_6_usa"""
from sqlalchemy import (create_engine)
from relationship_state import Base, State
from relationship_city import City
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

    newState = State()
    newState.name = 'California'
    newCity = City()
    newCity.name = 'San Francisco'
    newState.cities.append(newCity)
    session.add(newState)
    session.add(newCity)

    session.commit()
    session.close()
