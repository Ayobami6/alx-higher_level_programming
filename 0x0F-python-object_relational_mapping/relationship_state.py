#!/usr/bin/python3
""" States and cities relationship """

from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.orm import relationship, backref, declarative_base

meta = MetaData()
Base = declarative_base(metadata=meta)


class State(Base):
    """ State class

    Args:
        Base (Base): Base class
    """

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")
