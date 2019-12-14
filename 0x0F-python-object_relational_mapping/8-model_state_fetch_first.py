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
    # in this case output is going to be an element
    # because we are using first() method that return the first
    # element of the result of the query
    output = ses.query(State).order_by(State.id).first()
    if not (output):
        print("Nothing")
    else:
        print("{}: {}".format(output.id, output.name))
    ses.close()
