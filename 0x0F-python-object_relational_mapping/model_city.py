#!/usr/bin/python3
""" a python file that contains the class definition of a
City and an instance Base = declarative_base()"""
from sqlalchemy import Integer, String, Column, ForeignKey
from model_state import Base, State


class City(Base):
    """
    a class city that inherits from base
    """
    __tablename__ = 'cities'
    id = Column(
            Integer,
            primary_key=True,
            autoincrement=True,
            nullable=False)
    name = Column(
            String(128),
            nullable=False)
    state_id = Column(
            Integer,
            ForeignKey('states.id'),
            nullable=False)
