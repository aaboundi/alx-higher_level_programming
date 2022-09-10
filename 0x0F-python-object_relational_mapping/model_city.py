#!/usr/bin/python3
"""Definition of the City class"""

"""model_city.py"""

from sqlalchemy import Column, Integer, String, ForeignKey  # noqa: E402
from sqlalchemy.ext.declarative import declarative_base  # noqa: E402
from sqlalchemy.orm import relationship  # noqa: E402

Base = declarative_base()


class City(Base):
    """
    Class City.
    """

    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
