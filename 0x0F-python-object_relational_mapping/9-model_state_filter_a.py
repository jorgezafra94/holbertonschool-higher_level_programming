#!/usr/bin/python3
"""Start link class to table in database
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
    # output is going to be the result of the
    # query SELCT * FROM states; ORDER BY id
    # so output is going to be a list of objects
    output = ses.query(State).order_by(State.id)
    for elem in output:
        if ('a' in elem.name):
            print("{}: {}".format(elem.id, elem.name))
    ses.close()
