#!/usr/bin/python3
"""Module - 13-model_state_delete_a"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


def delete_states(username, password, db_name):
    """Function deletes all states in the database
    Args:
        -username
        -password
        -db_name
    """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                            username, password, db_name), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    states_to_del = session.query(State).filter(State.name.like('%a')).all()

    if states_to_del:
        for state in states_to_del:
            session.delete(state)

    session.commit()
    session.close()


if __name__ == "__main__":
    """The main function"""
    if len(sys.argv) != 4:
        print("Usage: python <username> <password> <database>")
        exit()

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    delete_states(username, password, db_name)
