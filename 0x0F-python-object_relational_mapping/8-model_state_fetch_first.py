#!/usr/bin/python3
"""Module: 7-model_state_fetch_all - contains a function that
   lists all states objects in the database hbtn_0e_6_usa
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys
from model_state import Base, State


def states(username, password, db_name):
    """The state function - lists all states in the database
    Args:
        - username
        - password
        - db_name
    """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                            username, password, db_name), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).all()
    print("{}: {}".format(states[0].id, states[0].name))

    session.close()


if __name__ == "__main__":
    """The main checker"""
    if len(sys.argv) != 4:
        print("Usage: python <script> <username> <password> <db_name>")
        sys.exit(1)
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    states(username, password, db_name)
