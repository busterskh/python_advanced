"""
Напишите GET-эндпоинт /ps, который принимает на вход аргументы командной строки,
а возвращает результат работы команды ps с этими аргументами.
Входные значения эндпоинт должен принимать в виде списка через аргумент arg.

Например, для исполнения команды ps aux запрос будет следующим:

/ps?arg=a&arg=u&arg=x
"""

import shlex
import subprocess

from flask import Flask, request

app = Flask(__name__)


@app.route("/ps", methods=["GET"])
def ps() -> str:
    ps_list = request.args.getlist('arg')
    ps_list = ''.join(ps_list)

    clean_user_cmd = shlex.quote(ps_list)
    command = shlex.split(f"ps {clean_user_cmd}")
    command_result = subprocess.run(command, capture_output=True, text=True).stdout

    return f'{command_result}'


if __name__ == "__main__":
    app.run(debug=True)
