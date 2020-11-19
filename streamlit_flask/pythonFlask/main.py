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
        bookListObject.append(Book(**book))

print('book list ' , bookListObject.__str__())
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


@app.route("/api/books/<id>")
def api_books_id(id):
    lesBook = Book.from_json(booksJson)
    print("les books : " + book)
    # for i in lesBook:
    #     if booksJson[i].id == id:
    #         print(booksJson)
    return 'test'



if __name__ == '__main__':
    app.run(debug=True)
