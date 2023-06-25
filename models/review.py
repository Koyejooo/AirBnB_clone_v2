#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel, Base
from models.place import Place
from models.user import User
from sqlalchemy import String, ForeignKey


class Review(BaseModel, Base):
    """Represent and link to a MySQL table - "reviews",
    with the table columns represented as class attributes:
        a. text - A column for a str of max 1024 chars; CANNOT be null.
        a. place_id(FK) - A column for a str of max 60 chars; CANNOT be null.
        b. user_id(FK) - A column for a str of max 60 chars; CANNOT be null.
    """
    __tablename__ = 'reviews'

    place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    text = Column(String(1024), nullable=False)
