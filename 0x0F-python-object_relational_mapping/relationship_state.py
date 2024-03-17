#!/usr/bin/python3
"""Module - model_state: creates the database Base class"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """class State inherits from Base=declarative_base"""
    __tablename__ = 'states'

    id = Column("id", Integer, primary_key=True,
                autoincrement=True, nullable=False)
    name = Column("name", String(128), nullable=False)

    cities = relationship('City', back_populates='state', cascade='all, delete-orphan')
