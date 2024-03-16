#!/usr/bin/python3
"""Module - 12-model_state_update_id_2"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def update_state(username, password, db_name, state_name):
    """The function updates the database value at a given id
    Args:
        -username
        -password
        -db_name
        -state_name
    """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                            username, password, db_name), pool_pre_ping=True)

    Base.metadata.bind = engine
    Session = sessionmaker(engine)
    session = Session()

    state = session.query(State).filter_by(id=2).first()
    state.name = state_name
    session.commit()

    session.close()


if __name__ == "__main__":
    """main checker"""
    if len(sys.argv) != 4:
        print("Usage: python <username> <password> <database>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = "New Mexico"

    update_state(username, password, db_name, state_name)
