from flask import Flask, render_template, request
import random

from game_core import GameCore
from settings import get_random_number, Settings

app = Flask(__name__)
app.config.from_object('config')
core = GameCore()  # создаем экземляр игрового ядра

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        input_num = request.form['val']
        window_mes = core.check_number(input_num)
        return render_template('index.html', window_mes=window_mes, active_game=Settings.active_game)

    if request.method == 'GET':
        window_mes = core.START  # передаем вступительное сообщение
        return render_template('index.html', window_mes=window_mes, active_game=Settings.active_game)


@app.route('/restart')
def restart():
    Settings.checked_num.clear()
    Settings.count = 0
    Settings.number = get_random_number()
    window_mes = random.choice(core.WELCOME_MES)  # передаем вступительное сообщение
    Settings.active_game = True
    return render_template('index.html', window_mes=window_mes, active_game=Settings.active_game)


@app.route('/bonusgame', methods=['POST', 'GET'])
def bonus():
    if request.method == 'POST':
        window_mes = core.BONUS_GAME_MES
        return render_template('index.html', window_mes=window_mes, active_game=Settings.active_game)

    if request.method == 'GET':
        window_mes = random.choice(core.WELCOME_MES)  # передаем вступительное сообщение
        core.count = 0
        return render_template('index.html', window_mes=window_mes, active_game=Settings.active_game)


if __name__ == '__main__':
    app.run(debug=True)
