"""
The module that implements the connection to the database.
"""

from sqlalchemy import create_engine


class EngineDB():
    def __init__(self, type_db, driver_db, user_name_db, password_db, host_db,
                 port_db, name_db):
        self.type_db = type_db
        self.driver_db = driver_db
        self.user_name_db = user_name_db
        self.password_db = password_db
        self.host_db = host_db
        self.port_db = port_db
        self.name_db = name_db

    def connect_db(self):
        return create_engine(
            f'{self.type_db}+{self.driver_db}://{self.user_name_db}:{self.password_db}@{self.host_db}:{self.port_db}/{self.name_db}',
            echo=True)
