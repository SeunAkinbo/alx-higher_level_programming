#!/usr/bin/python3
'''Module - model.py'''

from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    '''Class state inherits from Base =  declarative_base'''
    __table__ = "states"

    id = Column(Integer, primary_key=True,
                nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
