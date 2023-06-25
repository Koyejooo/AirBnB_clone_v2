#!/usr/bin/python3
"""This module creates a new database engine"""
from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv
from sqlalchemy.schema import MetaData
from models.base_model import BaseModel


class DBStorage:
    """Define new DB storage engine"""
    __engine = None
    __session = None

    def __init__(self):
        """Create and define the engine"""
        engine_args = URL.create(mysql+mysqldb,\
                username=getenv('HBNB_MYSQL_USER'),\
                password=getenv('HBNB_MYSQL_PWD'),\
                host=getenv('HBNB_MYSQL_HOST'),\
                database=getenv('HBNB_MYSQL_DB'))
        self.__engine = create_engine(engine_args, pool_pre_ping=True)

        if getenv('HBNB_ENV') == 'test':
            BaseModel.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """Query current DB session for all objects (i.e table columns) of a
        given class (i.e representation of SQL table).
        SPECS:
            a. If no class is given, query will be performed on all objects
               (i.e tbl columns) of all respective classes (i.e tables) in DB.
        RETURN A dictionary with the following format:
            key   = '<class-name>.<object-id>'; and
            value = the respective class objects
        """

        with self.__session as session:
            if cls is not None:
                dict_of_objects = {f'{type(cls).__name__}.{class_objs.id}':\
                        class_objs for class_objs in session.query(cls)}
            return (dict_of_objects)
            else:
                for classes in BaseModel.__subclasses__():
                    dict_of_objects = {f'{type(classes).__name__}.\
                            {class_objs.id}': class_objs for class_objs\
                            in session.query(classes)}
                return (dict_of_objects)
    
    def new(self, obj):
        """Add the object passed as 'obj' into the current DB session"""
        with self.__session as session:
            session.add(obj)

    def save(self):
        """Commit all changes of the current DB session"""
        with self.__session as session:
            session.commit(self)

    def delete(self, obj=None):
        """Delete the object passed as 'obj' if it is not none"""
        with self.__session as session:
            if obj is not None:
                session.delete(obj)
    
    def reload(self):
        """This function performs 2 tasks:
            1. Create all tables in the database; and
            2. Create a thread-safe session (using sessionmaker) from
               the engine created at initialization.
        """
        from models.amenity import Amenity
        from models.city import City
        from models.place import Place
        from models.review import Review
        from models.state import State
        from models.user import User

        Base.metadata.create_all(self.__engine)

        Session = scoped_session(sessionmaker(bind=self.__engine,
                                              expire_on_commit=False))
        self.__session = Session()
