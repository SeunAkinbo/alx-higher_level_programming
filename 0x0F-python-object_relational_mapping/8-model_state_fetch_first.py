#!/usr/bin/python3
"""Module: 8-model_state_fetch_first - contains a function that
   lists the first state object in the database hbtn_0e_6_usa
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys
from model_state import Base, State


def first_state(username, password, db_name):
    """The state function - outputs the first state in the database
    Args:
        - username
        - password
        - db_name
    """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                            username, password, db_name), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).first()

    if state is None:
        print("Nothing")
    else:
        print("{}: {}".format(state.id, state.name))

    session.close()


if __name__ == "__main__":
    """The main checker"""
    if len(sys.argv) != 4:
        print("Usage: python <script> <username> <password> <db_name>")
        sys.exit(1)
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    first_state(username, password, db_name)
