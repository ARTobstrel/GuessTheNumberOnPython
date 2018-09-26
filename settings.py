import random

def get_random_number():
    """Получение случайного числа"""
    num = random.randint(1, 100)
    return num


class Settings():
    """Все игровые настройки"""

    active_game = False
    bonus_game = False
    count = 0
    checked_num = set()
    number = 1




