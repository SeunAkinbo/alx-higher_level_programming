#!/usr/bin/python3
"""Module - 10-model_state_my_get: contains a function that prints
   state object of name parsed
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


def get_state(username, password, db_name, state_name):
    """The fuction prints the State object with the name
       passed as argument from the database

    Args:
        -username
        -password
        -db_name
        -state_name
    """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                            username, password, db_name), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).filter_by(name=state_name)

    if states is None:
        print("Not found")
    else:
        for state in states:
            print(state.id)

    session.close()


if __name__ == "__main__":
    """The main checker"""
    if len(sys.argv) != 5:
        print("Usage: python <script> <username> <password> <db_name> <state>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    get_state(username, password, db_name, state_name)
