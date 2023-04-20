#!/usr/bin/python3
"""
script that lists all State objects from the database hbtn_0e_6_usa
"""
import sys
import sqlalchemy as db
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

# Database Configuration
user = sys.argv[1]
passwd = sys.argv[2]
host = 'localhost'
port = 3306
database = sys.argv[3]

if __name__ == "__main__":
    engine = db.create_engine(
        "mysql://{}:{}@{}:{}/{}".format(user, passwd, host, port, database))

    Session = sessionmaker(bind=engine)
    Session = Session()
    result = Session.query(State).all()
    for obj in result:
        print("{}: {}".format(obj.id, obj.name))
