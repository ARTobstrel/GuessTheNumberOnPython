import random

from game_messages import GameMessages


class GameCore(GameMessages):
    """ядро игры, вся логика игры обрабатывается в этом классе"""

    def __init__(self):
        self.computer_guess_number()  # инициализация метода загадывания числа компьютером
        self.checked_num = set()  # сет введенных чисел
        self.count = 0  # счетчик попыток

    def computer_guess_number(self):
        """здесь компьютер загадывает число"""

        self.number = random.randint(1, 100)
        print(self.number)

    def output_checked_num(self):
        """здесь происходит перебор всех элементов введенных чисел(сета), с сохранением в переменную"""
        nums = ''
        for num in self.checked_num:
            nums = nums + '{}, '.format(num)
        nums = nums[:len(nums) - 2]
        return nums

    def check_number(self, input_num):
        """проверка введеного числа и загаданного числа"""

        if input_num == None:
            text_input = GameMessages.SPAM_MES
            return text_input

        try:
            input_num = int(input_num)
        except:
            # Not a string
            text_input = GameMessages.NOT_NUMBER_MES
            return text_input
        else:

            if input_num < 1 or input_num > 100:
                # Out of range
                text_input = GameMessages.OUT_OF_RANGE_MES
                return text_input

            if input_num == self.number:
                # Victory
                self.checked_num.add(input_num)
                self.count += 1
                text_input = GameMessages.WIN_MES.format(self.number, self.count, self.output_checked_num())
                return text_input

            if input_num in self.checked_num:
                text_input = GameMessages.ALREDY_EXISTS_MES.format(input_num)
                return text_input

            if input_num > self.number:
                text_input = GameMessages.LESS_MES

            if input_num < self.number:
                text_input = GameMessages.MORE_MES

            self.checked_num.add(input_num)
            self.count += 1
            return text_input
