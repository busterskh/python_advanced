"""
Давайте напишем свое приложение для учета финансов.
Оно должно уметь запоминать, сколько денег мы потратили за день,
    а также показывать затраты за отдельный месяц и за целый год.

Модифицируйте  приведенный ниже код так, чтобы у нас получилось 3 endpoint:
/add/<date>/<int:number> - endpoint, который сохраняет информацию о совершённой за какой-то день трате денег (в рублях, предполагаем что без копеек)
/calculate/<int:year> -- возвращает суммарные траты за указанный год
/calculate/<int:year>/<int:month> -- возвращает суммарную трату за указанный месяц

Гарантируется, что дата для /add/ endpoint передаётся в формате
YYYYMMDD , где YYYY -- год, MM -- месяц (число от 1 до 12), DD -- число (от 01 до 31)
Гарантируется, что переданная дата -- корректная (никаких 31 февраля)
"""
import time
from flask import Flask

app = Flask(__name__)

storage = {('2022', '01', '31'): 2000,
                        ('2022', '02', '03'): 2000,
                        ('2022', '03', '15'): 2000
                        }


@app.route("/add/<date>/<int:number>")
def add(date: str, number: int):
    global storage
    date = (date[:4], date[4:6], date[6:])
    try:
        _ = time.strptime('/'.join(date), '%Y/%m/%d')
        storage[date] = storage.get(date, 0) + number
        return f'Запись внесена!'
    except ValueError:
        return 'Введенная дата не корректна. Введите дату в формате YYYYMMDD'


@app.route("/calculate/<int:year>")
def calculate_year(year: int):
    total_summ = 0
    for key, value in storage.items():
        if year == int(key[0]):
            total_summ += value

    if total_summ > 0:
        return f'Общая сумма потраченная за {year} год: {total_summ}'


@app.route("/calculate/<int:year>/<int:month>")
def calculate_month(year: int, month: int):
    total_summ = 0
    for key, value in storage.items():
        if year == int(key[0]):
            if month == int(key[1]):
                total_summ += value

    if total_summ > 0:
        return f'Общая сумма потраченная за {month} месяц {year} года: {total_summ}'


if __name__ == "__main__":
    app.run(debug=True)
