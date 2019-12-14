#!/usr/bin/python3
"""
ORM queries that modify the databse

"""

import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    # lets create a Session object
    ses = Session()
    # adding a new element in the table
    Louisiana = State(name='Louisiana', id=6)
    ses.add(Louisiana)
    print(Louisiana.id)
    # refresh table
    ses.commit()
    ses.close()
