"""
Description of the model for the database of two entities: a book and a writer.
"""


from sqlalchemy import Column, ForeignKey, Integer, String, BigInteger
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from db_connect import EngineDB

Base = declarative_base()


class Book(Base):
    __tablename__ = 'book'

    id = Column(Integer, primary_key=True)
    writer_id = Column(Integer, ForeignKey('writer.id'), nullable=False)
    title = Column(String(300), nullable=False)
    number_of_evaluations = Column(Integer, server_default="0", nullable=False)
    summ_evaluations = Column(BigInteger, server_default="0", nullable=False)


class Writer(Base):
    __tablename__ = 'writer'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    patronymic = Column(String(100), nullable=False)
    book_id = Column(Integer, ForeignKey('book.id'))


engine = EngineDB('postgresql', 'psycopg2', 'postgres', 'testpass',
                  'localhost', '5432', 'test_api_db')
engine = engine.connect_db()
Base.metadata.create_all(engine)
