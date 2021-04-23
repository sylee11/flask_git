from flask import Flask, Response
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/a')
def a():
    return "Say"


if __name__ == '__main__':
    app.run()
