#!/usr/bin/python3
"""Script that adds the State object “Louisiana” to the database hbtn_0e_6_usa
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
    # Create a new instance of State and add it to the current database session
    new_instance = State(name="Louisiana")
    session.add(new_instance)
    session.commit()
    print(new_instance.id)
    session.close()
