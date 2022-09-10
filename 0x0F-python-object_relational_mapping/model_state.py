#!/usr/bin/python3
"""Definition of the State class"""

"""model_state.py"""

from sqlalchemy import Column, Integer, String # noqa: E402
from sqlalchemy.ext.declarative import declarative_base # noqa: E402

Base = declarative_base()


class State(Base):
    """
    Class State.
    __tablename__ (str): The name of the MySQL table to store States.
    id (sqlalchemy.Integer): The state's id.
    name (sqlalchemy.String): The state's name.
    """

    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
