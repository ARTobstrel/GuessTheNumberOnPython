from flask import Flask, render_template, request
from game_core import GameCore


app = Flask(__name__)
core = GameCore()  # создаем экземляр игрового ядра


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        # тут должны получать введенные данные методом пост
        q = 'метод пост не получает данные'
        window_mes = core.check_number(q)
        return render_template('index.html', window_mes=window_mes)

    if request.method == 'GET':
        window_mes = core.WELCOME_MES  # передаем вступительное сообщение
        return render_template('index.html', window_mes=window_mes)


if __name__ == '__main__':
    app.run(debug=True)
