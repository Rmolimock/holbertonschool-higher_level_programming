#!/usr/bin/python3
'''
    Lists row with given name
'''

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    user = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]
    my_state = sys.argv[4]
    connection = 'mysql+mysqldb://{}:{}@localhost:3306/{}'
    engine = create_engine(connection.format(user, passwd, db),
                           pool_pre_ping=True)

    session = sessionmaker(bind=engine)

    query = session().query(State).filter(State.name==my_state).first()

    if query:
        print(query.id)
    else:
        print("Not found")
    session().close()
