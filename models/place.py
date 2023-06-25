#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel
from models.city import City
from models.user import User
from sqlalchemy import Column, String, Integer, Float, ForeignKey


class Place(BaseModel):
    """Represent and link to a MySQL table - "places",
    with the table columns represented as class attributes:
        a. city_id(FK) - A column for a str of max 60 chars; CANNOT be null.
        b. user_id(FK) - A column for a str of max 60 chars; CANNOT be null.
        c. name - A column of a str of max 128 chars; CANNOT be null.
        d. description - A column for a str of max 1024 chars; CAN be null.
        e. number_rooms - A column for an int with def val 0; CANNOT be null.
        f. number_bathrooms - Same configurations as number_rooms.
        g. max_guest - A column for an int with def value 0; CANNOT be null.
        h. price_by_night - A column for an int wth def val 0; CANNOT be null.
        i. latitude - A column for a float; CAN be null.
        j. longitude - A column for a float; CAN be null.
    """
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []
