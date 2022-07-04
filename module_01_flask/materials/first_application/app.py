import datetime
from flask import Flask

app = Flask(__name__)
counter = 0


@app.route('/test')
def test_function():
   return 'Это тестовая страничка, ответ сгенерирован в %s' % \
                     datetime.datetime.now().utcnow()


@app.route('/hello/world')
def hello_world():
    return 'Hello, World!'


@app.route('/counter')
def counter_func():
    global counter
    counter += 1
    return f'Страничка открывалась {counter} раз'

