#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """Represent and link to a MySQL table - "users",
    with the table columns represented as class attributes:
        a. email - A column of a str of max 128 chars; CANNOT be null.
        b. password - A column of a str of max 128 chars; CANNOT be null.
        c. first_name - A column of a str of max 128 chars; CAN be null.
        d. last_name - A column of a str of max 128 chars; CAN be null.
    """
    __tablename__ = 'users'

    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
    # places = relationship("Place", cascade="all, delete", backref="user")
