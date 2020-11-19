from flask import Flask
from flask import request

app = Flask(__name__)


@app.route("/")
def index():
    return "hello world! <a href=\"/about\"> go about</a>"


@app.route('/about')
def about():
    return 'The about page'


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return "test ok"
    else:
        return "test no"


if __name__ == '__main__':
    app.run(debug=True)
