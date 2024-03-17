#!/usr/bin/python3
"""Module - 102-relationship_cities_states_list"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import City, Base
import sys


def all_cities(username, password, db_name):
    """The function lists all the city object in the database
    Args:
        -username
        -password
        -db_name
    """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                            username, password, db_name), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    cities = session.query(City).order_by(City.id).all()

    for city in cities:
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))

    session.close()


if __name__ == "__main__":
    """The main function"""
    if len(sys.argv) != 4:
        print("")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    all_cities(username, password, db_name)
