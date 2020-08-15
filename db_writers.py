from sqlalchemy.orm import sessionmaker
from db_models import Book, Writer, Base
from db_connect import EngineDB

engine = EngineDB().connect_db()
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


class BookCRUD():
    def __init__(self):
        pass
    
    def create(self):
        bookOne = Book(writer_id=1, title='Чистый')
        session.add(bookOne)
        session.commit()

    def read(self):
        books = session.query(Book).all()
        for book in books:
            print(book.title, book.writer_id,
                  (book.summ_evaluations / book.number_of_evaluations))

    def update(self):
        editedBook = session.query(Book).filter_by(book_id=1).one()
        editedBook.writer_id = 2
        session.add(editedBook)
        session.commit()

    def delete(self):
        bookToDelete = session.query(Book).filter_by(title='Чистый').one()
        session.delete(bookToDelete)
        session.commit()

class WriterCRUD():
    def __init__(self):
        pass
    
    def create(self):
        bookOne = Writer(first_name='s', last_name='p', patronymic='i', book_id=2)
        session.add(bookOne)
        session.commit()

    def read(self):
        books = session.query(Book).all()
        for book in books:
            print(book.title, book.writer_id,
                  (book.summ_evaluations / book.number_of_evaluations))

    def update(self):
        editedBook = session.query(Book).filter_by(book_id=1).one()
        editedBook.writer_id = 2
        session.add(editedBook)
        session.commit()

    def delete(self):
        bookToDelete = session.query(Book).filter_by(title='Чистый').one()
        session.delete(bookToDelete)
        session.commit()

session.close()
