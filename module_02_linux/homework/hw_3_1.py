"""
Напишите  flask endpoint, который показывал бы превью файла.
Он должен принимать на вход 2 параметра - SIZE (integer) и RELATIVE_PATH -
и выводить первые SIZE символов файла по указанному в RELATIVE_PATH пути.

Endpoint должен будет вернуть 2 строки.
В первой строке будет содержаться полезная информация о файле (его абсолютный путь и размер файла в символах).
После переноса строки будет приведено первые SIZE символов из файла:

<abs_path> <result_size><br>
<result_text>

где abs_path -- написанный жирным абсолютный путь до файла
result_size -- длина result_text в символах
result_text -- первые SIZE символов файла . Если размер файла больше SIZE, верните только первые SIZE символов

Перенос строки нужно осуществить с помощью html тэга <br>

PS в python абсолютный путь до файла можно узнать вот так
>>> import os
>>> print(os.path.abspath('<some_file_name>'))

"""
import os
from flask import Flask

app = Flask(__name__)


@app.route("/head_file/<int:size>/<path:relative_path>")
def head_file(size: int, relative_path: str):
    abs_path = os.path.join('/', relative_path)
    if os.path.exists(abs_path):
        with open(abs_path, 'r', encoding='utf-8') as file:
            text = file.read()
            if len(text) < size:
                result_text = text
            else:
                result_text = text[:size]
        result_size = len(text)
        return f'<b>{abs_path}</b> {result_size}<br>{result_text}'
    else:
        return f'<b>Файла не существует или путь недействительный.</b><br>' \
               f'Проверьте правильность введенного пути:<br>' \
               f'<i>{abs_path}</i>'


if __name__ == "__main__":
    app.run(debug=True)
