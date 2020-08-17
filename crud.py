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
        # Provides data about all entity objects book
        books = session.query(Book).all()
        return jsonify(books=[b.serialize for b in books])

    def get_book(self, id):
        # Basic book information
        books = session.query(Book).filter_by(id=id).one()
        return jsonify(books=books.serialize)

    def make_a_new_book(self, title):
        # book development, in particular the title
        added_book = Book(title=title)
        session.add(added_book)
        session.commit()
        return jsonify(Book=added_book.serialize)

    def update_book(self, id, title, evaluation):
        # Changing the book's basic data. This also includes changing the rating of the book.
        updated_book = session.query(Book).filter_by(id=id).one()
        if title:
            updated_book.title = title
        if evaluation:
            evaluation = int(evaluation)
            if 1 <= evaluation <= 5:
                updated_book.number_of_evaluations += 1
                updated_book.summ_evaluations += evaluation
                updated_book.rating = self.rating_book(
                    updated_book.summ_evaluations,
                    updated_book.number_of_evaluations)
            else:
                return f'The book with the id {id} was not updated. The evaluation is incorrect'
        session.add(updated_book)
        session.commit()
        return f'Updated a Book with id {id}'

    def delete_a_book(self, id):
        # Delete the base object of the book.
        book_to_delete = session.query(Book).filter_by(id=id).one()
        session.delete(book_to_delete)
        session.commit()
        return f'Removed Book with id {id}'

    def rating_book(self, summ_evaluations, number_of_evaluations):
        # Method for calculating the book rating.
        return round(summ_evaluations / number_of_evaluations)


class AuthorCRUD():
    """
    CRUD implementation for the Author entity.
    """
    def __init__(self):
        pass

    def get_authors(self):
        # Provides data about all entity objects author
        authors = session.query(Author).all()
        return jsonify(authors=[a.serialize for a in authors])

    def get_author(self, id):
        # Getting basic information about the author. This also includes the
        # provision of 5 top books by the author.
        query = session.query(Books, Book,
                              Author).filter_by(author_id=id).order_by(
                                  Book.rating.desc())
        query = query.join(Book, Book.id == Books.book_id)
        query = query.join(Author, Author.id == Books.author_id)
        top_five_books = []
        for books, book, author in query.limit(5):
            top_five_books.append(book.title)

        return jsonify(authors=author.serialize, top_five_books=top_five_books)

    def make_an_new_authors(self, first_name, last_name, patronymic):
        # Creating a new author.
        added_author = Author(first_name=first_name,
                              last_name=last_name,
                              patronymic=patronymic)
        session.add(added_author)
        session.commit()
        return jsonify(Author=added_author.serialize)

    def update_author(self, id, first_name, last_name, patronymic):
        # Updating basic information about the author.
        updated_author = session.query(Author).filter_by(id=id).one()
        if first_name:
            updated_author.first_name = first_name
        if last_name:
            updated_author.last_name = last_name
        if patronymic:
            updated_author.patronymic = patronymic
        session.add(updated_author)
        session.commit()
        return f'Updated a Author with id {id}'

    def delete_an_author(self, id):
        # Deleting an author from the database.
        author_to_delete = session.query(Author).filter_by(id=id).one()
        session.delete(author_to_delete)
        session.commit()
        return f'Removed Book with id {id}'


class BooksCRUD():
    """
    CRUD 
    """
    def __init__(self):
        pass

    def get_books(self):
        # Getting information about all books (actually existing-with a title,
        # author, and other attributes).
        books = session.query(Books).all()
        return jsonify(books=[b.serialize for b in books])

    def get_book(self, book_id):
        # Providing information about the book and its authors.
        query = session.query(Books, Book, Author).filter_by(book_id=book_id)
        query = query.join(Book, Book.id == Books.book_id)
        query = query.join(Author, Author.id == Books.author_id)
        authors = []
        for books, book, author in query:
            authors.append(' '.join(
                [author.last_name, author.first_name, author.patronymic]))
        if book.rating:
            return jsonify(id=book.id,
                           title=book.title,
                           rating=book.rating,
                           authors=authors)
        return jsonify(id=book.id,
                       title=book.title,
                       rating=book.rating,
                       authors=authors)

    def make_a_new_book(self, book_id, author_id):
        # Creating a real book object by linking information about the book
        # and the author.
        added_book = Books(book_id=book_id, author_id=author_id)
        session.add(added_book)
        session.commit()
        return jsonify(Books=added_book.serialize)

    def update_book(self, id, book_id, author_id):
        # Updating links.
        updated_book = session.query(Books).filter_by(id=id).one()
        if book_id:
            updated_book.book_id = book_id
        if author_id:
            updated_book.author_id = author_id
        session.add(updated_book)
        session.commit()
        return f'Updated a Book with id {id}'

    def delete_a_book(self, book_id):
        # Deleting links.
        book_to_delete = session.query(Books).filter_by(book_id=book_id).all()
        session.delete(book_to_delete)
        session.commit()
        return f'Removed Books with id {id}'
