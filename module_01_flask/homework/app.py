import datetime
from flask import Flask
import random
import os


app = Flask(__name__)
cars_list = ['Chevrolet', 'Renault', 'Ford', 'Lada']

cats_list = ['Корниш рекс',
             'Русская голубая',
             'Шотландская вислоухая',
             'Мэйн-Кун',
             'Манчкин'
             ]


file_name = 'war_and_peace.txt'
base_dir = os.path.dirname(os.path.abspath(file_name))

for path, _, file in os.walk(base_dir):
    if file_name in file:
        base_dir = os.path.join(path, file_name)

if os.path.isfile(base_dir):
    file = open(base_dir, 'r', encoding='utf-8')
    text = file.read()
    file.close()
else:
    text = None


@app.route('/hello_world')
def hello_world() -> str:

    return 'Привет, мир!'


@app.route('/cars')
def cars() -> str:
    global cars_list
    cars_str = ' '.join(cars_list)

    return cars_str


@app.route('/cats')
def cats() -> str:
    global cats_list
    cat = random.choice(cats_list)

    return cat


@app.route('/get_time/now')
def curr_time() -> str:
    current_time = datetime.datetime.now()

    return f'Точное время {current_time}'


@app.route('/get_time/future')
def time_after_hour() -> str:
    current_time_after_hour = datetime.datetime.now() + datetime.timedelta(hours=+1)

    return f'Точное время через час будет {current_time_after_hour}'


@app.route('/get_random_word')
def war_and_peace() -> str:
    global text

    if text is not None:
        return random.choice(text.split())
    else:
        return 'Файл не найден.'
