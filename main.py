from flask import Flask, render_template, request
from game_core import GameCore

app = Flask(__name__)
core = GameCore()  # создаем экземляр игрового ядра


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        q = request.form['val']
        window_mes = core.check_number(q)
        return render_template('index.html', window_mes=window_mes)

    if request.method == 'GET':
        window_mes = core.WELCOME_MES  # передаем вступительное сообщение
        core.count = 0
        return render_template('index.html', window_mes=window_mes)


@app.route('/restart')
def restart():
    core.checked_num.clear()
    core.count = 0
    core.computer_guess_number()
    window_mes = core.WELCOME_MES  # передаем вступительное сообщение
    return render_template('index.html', window_mes=window_mes)


if __name__ == '__main__':
    app.run(debug=True)
