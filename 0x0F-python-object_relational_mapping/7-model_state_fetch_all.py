#!/usr/bin/python3
"""Lists State objects from the database
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine(
            "mysql+mysqldb://{}:{}@localhost/{}"
            .format(sys.arg[1], sys.argv[2], sys.argv[3]),
            pool_pre_pint=True
            )
    session_maker = sessionmaker(bind=engine)
    session = session_maker()

    for state in session.query(State).order_by(State.id):
        print("{}: {}".format(state.id, state.name))
