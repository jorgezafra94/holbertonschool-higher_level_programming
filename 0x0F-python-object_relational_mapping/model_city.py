#!/usr/bin/python3
"""
class to use in call of ORM
this class is going to have a Foreignkey from class State
"""
from sqlalchemy import ForeignKey
from model_state import Base
from sqlalchemy import Column, Integer, String


class City(Base):
    """

    class that is going to run in the ORM

    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, autoincrement=True,
                nullable=False, unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, nullable=False, ForeignKey('states.id'))
