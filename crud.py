"""
Module for implementing CRUD classes/functions
"""

from flask import jsonify
from sqlalchemy.orm import sessionmaker

from db_setup.db_connect import EngineDB
from db_setup.db_models import Author, Base, Book, Books

engine = EngineDB().connect_db()
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


class BookCRUD():
    """
    CRUD implementation for the Book entity.
    """
    def __init__(self):
        pass

    def get_books(self):
        books = session.query(Book).all()
        return jsonify(books=[b.serialize for b in books])

    def get_book(self, id):
        books = session.query(Book).filter_by(id=id).one()
        return jsonify(books=books.serialize)

    def make_a_new_book(self, title):
        added_book = Book(title=title)
        session.add(added_book)
        session.commit()
        return jsonify(Book=added_book.serialize)

    def update_book(self, id, title):
        updated_book = session.query(Book).filter_by(id=id).one()
        if title:
            updated_book.title = title
        session.add(updated_book)
        session.commit()
        return 'Updated a Book with id %s' % id

    def delete_a_book(self, id):
        book_to_delete = session.query(Book).filter_by(id=id).one()
        session.delete(book_to_delete)
        session.commit()
        return 'Removed Book with id %s' % id


class AuthorCRUD():
    """
    CRUD implementation for the Author entity.
    """
    def __init__(self):
        pass

    def get_authors(self):
        authors = session.query(Author).all()
        return jsonify(authors=[a.serialize for a in authors])

    def get_author(self, id):
        authors = session.query(Author).filter_by(id=id).one()
        return jsonify(authors=authors.serialize)

    def make_an_new_authors(self, first_name, last_name, patronymic):
        added_author = Author(first_name=first_name,
                              last_name=last_name,
                              patronymic=patronymic)
        session.add(added_author)
        session.commit()
        return jsonify(Author=added_author.serialize)

    def update_author(self, id, first_name, last_name, patronymic):
        updated_author = session.query(Author).filter_by(id=id).one()
        if first_name:
            updated_author.first_name = first_name
        if last_name:
            updated_author.last_name = last_name
        if patronymic:
            updated_author.patronymic = patronymic
        session.add(updated_author)
        session.commit()
        return 'Updated a Author with id %s' % id

    def delete_an_author(self, id):
        author_to_delete = session.query(Author).filter_by(id=id).one()
        session.delete(author_to_delete)
        session.commit()
        return 'Removed Book with id %s' % id
