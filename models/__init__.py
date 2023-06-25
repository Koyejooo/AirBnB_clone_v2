#!/usr/bin/python3
"""This module instantiates an object of one of the storage engines,
based on a a condition.
"""
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage
from os import getenv


if getenv('HBNB_TYPE_STORAGE') == 'db':
    storage = DBStorage()
else:
    storage = FileStorage()
storage.reload()
