#!/usr/bin/python3
"""Module - model_city"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from model_state import Base


class City(Base):
    """class City creates a new table in the database
    Inheritance:
        - Base: declarative_base from model_state
    """
    __tablename__ = 'cities'
    
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    name = Column("name", String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("state.id"), nullable=False)
    
    state = relationship("State", back_populates="cities")
