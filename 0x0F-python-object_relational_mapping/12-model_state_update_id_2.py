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
    output = ses.query(State).filter(State.id == 2)
    # if you want to reset the autoincrement use:
    # ALTER TABLE states AUTO_INCREMENT = 1;
    for elem in output:
        elem.name = "New Mexico"
    ses.commit()
    ses.close()
