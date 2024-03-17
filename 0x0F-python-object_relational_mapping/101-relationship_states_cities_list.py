#!/usr/bin/python3
"""Module - 101-relationship_states_cities_list.py"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City
import sys


def states_and_cities(username, password, db_name):
    """The function lists all the states and cities in the database
    Args:
        -username
        -password
        -db_name
    """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                            username, password, db_name), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    locations = session.query(State).join(City).order_by(State.id).all()

    for location in locations:
        print("{}: {}".format(location.id, location.name))
        for city in location.cities:
            print("\t{}: {}".format(city.id, city.name))

    session.close()


if __name__ == "__main__":
    """The main function"""
    if len(sys.argv) != 4:
        print("Usage: python <script> <username> <password> <database>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    states_and_cities(username, password, db_name)
