#!/usr/bin/python3
"""
ORM queries that modify the databse

"""

import sys
from model_state import Base, State
from model_city import City
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
    # JOIN IN ORM
    output = ses.query(State.name, City.id, City.name)\
                .join(City, State.id == City.state_id).order_by(City.id)
    for row in output:
        print("{}: ({}) {}".format(row[0], row[1], row[2]))
    ses.close()
