#!/usr/bin/python3
'''
    Lists row.name with the letter 'a' in a given database
'''

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    user = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]
    connection = 'mysql+mysqldb://{}:{}@localhost:3306/{}'
    engine = create_engine(connection.format(user, passwd, db),
                           pool_pre_ping=True)

    session = sessionmaker(bind=engine)

    query = session().query(State).filter(State.name.ilike("%a%")).\
        order_by(State.id).all()

    for item in query:
        print("{}: {}".format(item.id, item.name))
