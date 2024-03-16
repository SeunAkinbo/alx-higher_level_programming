#!/usr/bin/python3
"""Module: 14-model_city_fetch_by_state"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State, Base
from model_city import City
import sys


def cities(username, password, db_name):
    """The function prints all the cities in the database"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                            username, password, db_name), pool_pre_ping=True)

    Base.metadata.bind = engine
    Session = sessionmaker(bind=engine)
    session = Session()

    cities = session.query(City).order_by(City.id).all()

    if cities:
        for city in cities:
            print("{}: {}".format(city.id, city.name))

    session.close()


if __name__ == '__main__':
    """The main function"""
    if len(sys.argv) != 4:
        print("Usage: python <script> <username> <password> <db_name>")
        sys.exit(1)
    
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    
    cities(username, password, db_name)
