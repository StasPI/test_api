"""
Module that implements the connection to the database.

You need to provide data to access an empty database.
"""

from sqlalchemy import create_engine


class EngineDB():
    type_db = 'postgresql'
    driver_db = 'psycopg2'
    user_name_db = 'postgres'
    password_db = 'testpass'
    host_db = 'localhost'
    port_db = '5432'
    name_db = 'test_api_db'
        
    def __init__(self):
        pass


    def connect_db(self):
        return create_engine(
            f'{self.type_db}+{self.driver_db}://{self.user_name_db}:{self.password_db}@{self.host_db}:{self.port_db}/{self.name_db}',
            echo=True)
