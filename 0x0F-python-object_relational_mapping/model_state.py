#!/usr/bin/python3
""" state table mapper class
"""


from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.orm import declarative_base

meta = MetaData()
Base = declarative_base(metadata=meta)


class State(Base):

    """ State Class
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
