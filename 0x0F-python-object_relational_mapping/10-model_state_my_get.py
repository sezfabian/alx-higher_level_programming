#!/usr/bin/python3
"""
Lists the State object with the name passed as argument
from the database hbtn_0e_6_usa.
Usage: ./7-model_state_fetch_all.py <mysql username> /
                                    <mysql password> /
                                    <database name> /
                                    <state name searched>
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State


if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    mystate = "%" + sys.argv[4] + "%"

    result = session.query(State).filter(
        State.name.like(mystate)).first()
    if result:
        print("{}".format(result.id))
    else:
        print("Not Found")
