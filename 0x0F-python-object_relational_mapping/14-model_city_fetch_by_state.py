#!/usr/bin/python3
"""
 prints all City objects from the database hbtn_0e_14_usa
"""
from sqlalchemy import (create_engine)
from model_state import Base, State
from model_city import Base, City
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

    for city in session.query(City).join(State).order_by(City.id).all():
        print("{}: ({}) {}".format(city.state.name, city.id, city.name))
    
    session.close()
