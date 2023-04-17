#!/usr/bin/python3
"""Script that deletes all State objects with a name containing the letter a
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
    # Query all the instances with name containing 'a'
    instances = session.query(State).filter(State.name.like('%a%')).all()
    # delete all the instances with name containing 'a'
    for inst in instances:
        session.delete(inst)
    # commit the changes
    session.commit()
    # close the session
    session.close()
