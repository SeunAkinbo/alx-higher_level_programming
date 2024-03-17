#!/usr/bin/python3
"""Module - model_city"""

from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base, State


class City(Base):
    """class City creates a new table in the database
    Inheritance:
        - Base: declarative_base from model_state
    """
    __tablename__ = 'cities'

    id = Column("id", Integer, unique=True, primary_key=True)
    name = Column("name", String(128), nullable=False)
    state_id = Column(Integer, ForeignKey(State.id), nullable=False)
