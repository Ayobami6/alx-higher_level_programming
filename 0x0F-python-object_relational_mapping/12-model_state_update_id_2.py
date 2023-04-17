#!/usr/bin/python3
"""Script that changes the name of a State object of id 2 to New Mexico
    from the database hbtn_0e_6_usa
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
    # Query the instance with id = 2 and update the name
    instance = session.query(State).filter(State.id == 2).first()
    instance.name = "New Mexico"
    session.commit()
    session.close()
