#!/usr/bin/python3
"""
class to use in call of ORM
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """

    class that is going to run in the ORM

    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True,
                nullable=False, unique=True)
    name = Column(String(128), nullable=False)

    cities = relationship("City", cascade='delete', backref="state")
