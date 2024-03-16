#!/usr/bin/python3
"""Module - 11-model_state_insert"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


def add_state(username, password, db_name, state_name):
    """The fuction add a State object "Louisiana"
       to the database

    Args:
        -username
        -password
        -db_name
        -state_name
    """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                            username, password, db_name), pool_pre_ping=True)

    Base.metadata.bind = engine
    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State(name=state_name)
    session.add(new_state)
    session.commit()

    print(new_state.id)

    session.close()


if __name__ == "__main__":
    """The main checker"""
    if len(sys.argv) != 4:
        print("Usage: python <script> <username> <password> <db_name>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = 'Louisiana'

    add_state(username, password, db_name, state_name)
