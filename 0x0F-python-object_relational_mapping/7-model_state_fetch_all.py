#!/usr/bin/python3
"""
script that lists all State objects from the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

# Database Configuration
user = sys.argv[1]
passwd = sys.argv[2]
host = 'localhost'
port = 3306
database = sys.argv[3]

if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@{}:{}/{}"
        .format(user, passwd, host, port, database), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    Session = Session()
    result = Session.query(State).all()
    for state in result:
        print("{}: {}".format(state.id, state.name))
