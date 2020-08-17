from flask import Flask, request

from crud import AuthorCRUD, BookCRUD, BooksCRUD

app = Flask(__name__)
"""
API functions for the book entity.
"""
book = BookCRUD()


@app.route('/')
@app.route('/api/book', methods=['GET', 'POST'])
def book_function():
    if request.method == 'GET':
        return book.get_books()
    elif request.method == 'POST':
        title = request.args.get('title', '')
        return book.make_a_new_book(title)


@app.route('/api/book/', methods=['GET', 'PUT', 'DELETE'])
def book_function_id():
    if request.method == 'GET':
        id = request.args.get('id')
        return book.get_book(id)

    elif request.method == 'PUT':
        id = request.args.get('id')
        title = request.args.get('title')
        evaluation = request.args.get('evaluation')
        return book.update_book(id, title, evaluation)

    elif request.method == 'DELETE':
        id = request.args.get('id')
        return book.delete_a_book(id)


"""
API functions for the author entity.
"""
author = AuthorCRUD()


@app.route('/')
@app.route('/api/author', methods=['GET', 'POST'])
def autor_function():
    if request.method == 'GET':
        return author.get_authors()
    elif request.method == 'POST':
        first_name = request.args.get('first_name')
        last_name = request.args.get('last_name')
        patronymic = request.args.get('patronymic')
        return author.make_an_new_authors(first_name, last_name, patronymic)


@app.route('/api/author/', methods=['GET', 'PUT', 'DELETE'])
def autor_function_id():
    if request.method == 'GET':
        id = request.args.get('id')
        return author.get_author(id)

    elif request.method == 'PUT':
        id = request.args.get('id')
        first_name = request.args.get('first_name')
        last_name = request.args.get('last_name')
        patronymic = request.args.get('patronymic')
        return author.update_author(id, first_name, last_name, patronymic)

    elif request.method == 'DELETE':
        id = request.args.get('id')
        return author.delete_an_author(id)


"""
API functions for the relationship table.
"""
books = BooksCRUD()


@app.route('/')
@app.route('/api/books', methods=['GET', 'POST'])
def books_function():
    if request.method == 'GET':
        return books.get_books()
    elif request.method == 'POST':
        book_id = request.args.get('book_id', '')
        author_id = request.args.get('author_id', '')
        return books.make_a_new_book(book_id, author_id)


@app.route('/api/books/', methods=['GET', 'PUT', 'DELETE'])
def books_function_id():
    if request.method == 'GET':
        book_id = request.args.get('id')
        return books.get_book(book_id)

    elif request.method == 'PUT':
        id = request.args.get('id')
        book_id = request.args.get('book_id', '')
        author_id = request.args.get('author_id', '')
        return books.update_book(id, book_id, author_id)

    elif request.method == 'DELETE':
        id = request.args.get('id')
        return books.delete_a_book(id)


"""
Run host_port
"""
if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=4996)
