#!/usr/bin/python3
"""Module - 100-relationship_states_cities"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City
import sys


def create_state_city(username, password, db_name):
    """The function creates the State California with the city San Francisco"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                            username, password, db_name), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    addState = State(name='California')
    addCity = City(name='San Francisco')

    addState.cities.append(addCity)

    session.add(addState)
    session.commit()


if __name__ == "__main__":
    """The main function"""
    if len(sys.argv) != 4:
        print("Usage: python <script> <username> <password> <database>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    create_state_city(username, password, db_name)
