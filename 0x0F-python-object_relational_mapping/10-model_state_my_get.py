#!/usr/bin/python3
"""Script that prints the State object with the name passed as argument
    """

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # create database engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]))
    # Set up the tables in the database
    Base.metadata.create_all(engine)
    # Configuring session
    Session = sessionmaker(bind=engine)
    session = Session()
    # Query all instance for the name passed as argument
    instance = session.query(State).filter(State.name == argv[4]).first()
    if instance:
        print(instance.id)
    else:
        print("Not found")
    session.close()
