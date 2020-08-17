"""
Description of the model for the database of two entities: a book, an author.
"""

from sqlalchemy import (BigInteger, Column, ForeignKey, Integer, SmallInteger,
                        String)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from db_setup.db_connect import EngineDB

Base = declarative_base()


class Book(Base):
    """ Book essence """
    __tablename__ = 'book'

    id = Column(Integer, primary_key=True)
    title = Column(String(300), nullable=False)
    number_of_evaluations = Column(Integer, server_default="0", nullable=False)
    summ_evaluations = Column(BigInteger, server_default="0", nullable=False)
    rating = Column(SmallInteger, server_default="0", nullable=False)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'number_of_evaluations': self.number_of_evaluations,
            'summ_evaluations': self.summ_evaluations,
            'rating': self.rating
        }


class Author(Base):
    """ Essence of the book's author """
    __tablename__ = 'author'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    patronymic = Column(String(100), nullable=False)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'platronymic': self.patronymic,
        }


class Books(Base):
    """ Consolidated implementation """
    __tablename__ = 'books'

    id = Column(BigInteger, primary_key=True)
    book_id = Column(Integer, ForeignKey('book.id'))
    author_id = Column(Integer, ForeignKey('author.id'))

    @property
    def serialize(self):
        return {
            'id': self.id,
            'book_id': self.book_id,
            'author_id': self.author_id,
        }


engine = EngineDB().connect_db()
Base.metadata.create_all(engine)
