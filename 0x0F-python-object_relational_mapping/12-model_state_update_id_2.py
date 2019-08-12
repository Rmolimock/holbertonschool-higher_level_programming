#!/usr/bin/python3
'''
   change the name value of a row in states
'''
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    username = sys.argv[1]
    psw = sys.argv[2]
    db_name = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, psw, db_name), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    state_obj = session.query(State).filter_by(id=2).first()
    if state_obj:
        state_obj.name = "New Mexico"
    session.commit()
    session.close()
