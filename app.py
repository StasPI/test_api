from flask import Flask, request

from crud import AuthorCRUD, BookCRUD

app = Flask(__name__)

# Connect to Database and create database session
"""
CRUD
"""

book = BookCRUD()
author = AuthorCRUD()
"""
API
"""


@app.route('/')
@app.route('/api/book', methods=['GET', 'POST'])
def booksFunction():
    if request.method == 'GET':
        return book.get_books()
    elif request.method == 'POST':
        title = request.args.get('title', '')
        return book.make_a_new_book(title)


@app.route('/api/book/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def bookFunctionId(id):
    if request.method == 'GET':
        return book.get_book(id)

    elif request.method == 'PUT':
        title = request.args.get('title')
        return book.update_book(id, title)

    elif request.method == 'DELETE':
        return book.delete_a_book(id)


@app.route('/')
@app.route('/api/author', methods=['GET', 'POST'])
def autorsFunction():
    if request.method == 'GET':
        return author.get_authors()
    elif request.method == 'POST':
        first_name = request.args.get('first_name')
        last_name = request.args.get('last_name')
        patronymic = request.args.get('patronymic')
        return author.make_an_new_authors(first_name, last_name, patronymic)


@app.route('/api/author/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def autorFunctionId(id):
    if request.method == 'GET':
        return author.get_author(id)

    elif request.method == 'PUT':
        first_name = request.args.get('first_name')
        last_name = request.args.get('last_name')
        patronymic = request.args.get('patronymic')
        return author.update_author(id, first_name, last_name, patronymic)

    elif request.method == 'DELETE':
        return author.delete_an_author(id)


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=4996)
