from flask import Flask, render_template, request
from game_core import GameCore
import random

app = Flask(__name__)
core = GameCore()  # создаем экземляр игрового ядра

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        q = request.form['val']
        window_mes = core.check_number(q)
        active_game = core.active_game
        return render_template('index.html', window_mes=window_mes, active_game=active_game)

    if request.method == 'GET':
        window_mes = random.choice(core.WELCOME_MES)  # передаем вступительное сообщение
        core.count = 0
        active_game = core.active_game
        return render_template('index.html', window_mes=window_mes, active_game=active_game)


@app.route('/restart')
def restart():
    core.checked_num.clear()
    core.count = 0
    core.computer_guess_number()
    window_mes = random.choice(core.WELCOME_MES)  # передаем вступительное сообщение
    active_game = True
    return render_template('index.html', window_mes=window_mes, active_game=active_game)


@app.route('/bonusgame', methods=['POST', 'GET'])
def bonus():
    if request.method == 'POST':
        window_mes = core.BONUS_GAME_MES
        return render_template('index.html', window_mes=window_mes)


if __name__ == '__main__':
    app.run(debug=True)
