import datetime
from flask import Flask
import random

app = Flask(__name__)
current_time = datetime.datetime.now()


@app.route('/hello_world')
def hello_world():
    return 'Привет, мир!'


@app.route('/cars')
def cars():
    return 'Chevrolet, Renault, Ford, Lada'


@app.route('/cats')
def cats():
    cats_list = ['Корниш рекс',
                 'Русская голубая',
                 'Шотландская вислоухая',
                 'Мэйн-Кун',
                 'Манчкин'
                 ]
    return random.choice(cats_list)


@app.route('/get_time/now')
def curr_time():
    global current_time
    return f'Точное время {current_time}'


@app.route('/get_time/future')
def time_after_hour():
    global current_time
    current_time_after_hour = current_time + datetime.timedelta(hours=+1)
    return f'Точное время через час будет {current_time_after_hour}'


@app.route('/get_random_word')
def war_and_peace():
    with open('war_and_peace.txt', 'r', encoding='utf-8') as file:
        text = file.read()
        return random.choice(text.split())
