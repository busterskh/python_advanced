"""
Напишите GET-эндпоинт /uptime, который в ответ на запрос будет выводить строку вида f"Current uptime is {UPTIME}",
где UPTIME — uptime системы (показатель того, как долго текущая система не перезагружалась).

Сделать это можно с помощью команды uptime.
"""

import shlex
import subprocess
from flask import Flask, request

app = Flask(__name__)


@app.route("/uptime", methods=['GET'])
def uptime() -> str:
    command_str = request.args.get('arg')
    command = shlex.split(command_str)
    command_result = subprocess.run(command, capture_output=True, text=True).stdout

    result = command_result.split()
    result = ' '.join(result[1:5])
    result = result.replace(',', '')

    return f"{result}"


if __name__ == '__main__':
    app.run(debug=True)
