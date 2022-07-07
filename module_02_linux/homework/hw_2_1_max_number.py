"""
Реализуйте endpoint, с url, начинающийся с  /max_number ,
в который можно будет передать список чисел, перечисленных через / .
Endpoint должен вернуть текст "Максимальное переданное число {number}",
где number, соответственно, максимальное переданное в endpoint число,
выделенное курсивом.
"""

from flask import Flask

app = Flask(__name__)


@app.route("/max_number/<path:numbers>")
def max_number(numbers):
    """
    Endpoint вернет текст "Максимальное переданное число {number}",
    где number, максимальное переданное в endpoint число,
    выделенное курсивом.
    """
    try:
        numbers = [int(j) for j in numbers.split('/')]
        number = max(numbers)
        return f'Максимальное переданное число {number}'
    except ValueError:
        return 'Не все введенные данные являются целыми числами.'


if __name__ == "__main__":
    app.run(debug=True)
