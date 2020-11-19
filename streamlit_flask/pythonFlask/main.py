from flask import Flask, render_template, jsonify
from flask import request
import json
from model.Book import Book

app = Flask(__name__)

booksJson = [{'id': 1, 'titre': 'un titre'}, {'id': 2, 'titre': 'un autre titre random'}]
bookListObject = []
with open('json/books.json', 'r') as json_book:
    book_data = json.loads(json_book.read())
    for book in book_data:
        # print("book : ", book)
        # print("\n")
        # print(json.dumps(book))
        try:
            bookListObject.append(
                Book(**book)
            )
        except:
            pass

print('book list ', bookListObject.__str__())


@app.route("/")
@app.route("/index/")
def index():
    return render_template('index.html', title="Books", titleh1="hello my app")


@app.route("/ma_route/")
def name():
    return render_template('name.html', name="hello name")


@app.route("/books/")
def books():
    return render_template('books.html', books="books")


@app.route("/api/books/")
def api_books():
    return jsonify(booksJson)


@app.route("/api/books/id/<id>")
def api_books_id(id):
    for book in bookListObject:
        # print("book isbn" + book.isbn)
        if book.isbn == id:
            theBook = book
        else:
            pass
    return render_template('book.html', book=theBook)


@app.route("/api/books/title/<string:title>")
def api_books_title(title):
    global theBookTitle
    for book in bookListObject:
        if book.title == title:
            theBook = book
        else:
            pass
    return render_template('book.html', book=theBook)


if __name__ == '__main__':
    app.run(debug=True)
