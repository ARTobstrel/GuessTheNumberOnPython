import random

from game_messages import GameMessages


class GameCore(GameMessages):
    """ядро игры, вся логика игры обрабатывается в этом классе"""

    def __init__(self):
        self.computer_guess_number()  # инициализация метода загадывания числа компьютером
        self.checked_num = set()  # сет введенных чисел

    def computer_guess_number(self):
        """здесь компьютер загадывает число"""

        self.number = random.randint(1, 100)
        print(self.number)

    def check_number(self, input_number):
        """проверка введеного числа и загаданного числа"""

        try:
            input_number = int(input_number)
        except:
            text_input = GameMessages.NOT_NUMBER_MES
            return text_input
        else:

            if input_number == self.number:
                text_input = GameMessages.WIN_MES.format(self.number)

            if input_number > self.number:
                text_input = GameMessages.LESS_MES

            if input_number < self.number:
                text_input = GameMessages.MORE_MES

            if input_number in self.checked_num:
                text_input += GameMessages.ALREDY_EXISTS_MES.format(input_number)

            self.checked_num.add(input_number)
            return text_input
