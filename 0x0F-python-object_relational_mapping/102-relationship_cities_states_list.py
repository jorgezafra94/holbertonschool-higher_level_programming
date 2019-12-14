#!/usr/bin/python3
"""
ORM queries that modify the databse

"""

import sys
from relationship_state import Base, State
from relationship_city import City
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
    out = ses.query(City).order_by(City.id)
    for ciudad in out:
        print("{}: {} -> {}".format(ciudad.id, ciudad.name, ciudad.state.name))
    ses.close()
