import random

from game_messages import GameMessages
from settings import Settings


class GameCore(GameMessages, Settings):
    """ядро игры, вся логика игры обрабатывается в этом классе"""

    def output_checked_num(self):
        """здесь происходит перебор всех элементов введенных чисел(сета), с сохранением в переменную"""
        nums = ''
        for num in Settings.checked_num:
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
            # Not string
            text_input = GameMessages.NOT_NUMBER_MES
            return text_input
        else:

            if input_num < 1 or input_num > 100:
                # Out of range
                text_input = GameMessages.OUT_OF_RANGE_MES
                return text_input

            # # не работает
            # if input_num == self.number and self.count < 3 or input_num == 99:
            #     return redirect(url_for('.bonus'))

            if input_num == Settings.number:
                # Victory
                Settings.checked_num.add(input_num)
                Settings.count += 1
                text_input = GameMessages.WIN_MES.format(Settings.number, Settings.count, self.output_checked_num())
                Settings.active_game = False
                return text_input

            if input_num in Settings.checked_num:
                text_input = random.choice(GameMessages.ALREDY_EXISTS_MES).format(input_num)
                return text_input

            if input_num > Settings.number:
                text_input = GameMessages.LESS_MES

            if input_num < Settings.number:
                text_input = GameMessages.MORE_MES

            Settings.checked_num.add(input_num)
            Settings.count += 1
            return text_input
