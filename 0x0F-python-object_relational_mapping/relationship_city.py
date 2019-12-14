#!/usr/bin/python3
"""
class to use in call of ORM
this class is going to have a Foreignkey from class State
"""
from sqlalchemy import ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from relationship_state import Base, State


class City(Base):
    """

    class that is going to run in the ORM

    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, autoincrement=True,
                nullable=False, unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
