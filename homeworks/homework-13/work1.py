"""
Задание 1. Карма.

Один буддист-программист решил создать свой симулятор жизни, в котором
нужно набрать 500 очков кармы (это константа), чтобы достичь просветления.
Каждый день вызывается специальная функция one_day(), которая возвращает количество
кармы от 1 до 7 и может с вероятностью 1 к 10 выкинуть одно из исключений:
    ● KillError,
    ● DrunkError,
    ● CarCrashError,
    ● GluttonyError,
    ● DepressionError.
(Исключения нужно создать самостоятельно, при помощи наследования от Exception.)

Напишите такую программу.
Функцию оберните в бесконечный цикл, выход из которого возможен только при накоплении
кармы до уровня константы.
Исключения обработайте и запишите в отдельный лог karma.log.
По итогу у вас может быть примерно такая структура программы:
    открываем файл
    цикл по набору кармы
        try
            карма += one_day()
        except(ы) с указанием классов исключений, которые нужно поймать
            добавляем запись в файл
    закрываем файл
"""
import random

MAX_SCORE = 500


class LiveException(Exception):
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return f"{self.text}"


class KillError(LiveException):
    def __init__(self):
        super().__init__('Вы кого-то убили!')


class DrunkError(LiveException):
    def __init__(self):
        super().__init__('Вы напились!')


class CarCrashError(LiveException):
    def __init__(self):
        super().__init__('Вы попали в аварию!')


class GluttonyError(LiveException):
    def __init__(self):
        super().__init__('Вы объелись!')


class DepressionError(LiveException):
    def __init__(self):
        super().__init__('Вы впали в депрессию!')


def one_day():
    """ Один день жизни. """
    if random.randint(1, 10) == 1:
        raise random.choice([KillError(), DrunkError(), CarCrashError(), GluttonyError(), DepressionError()])
    return random.randint(1, 7)


def game():
    """ Игра до победного конца. """
    karma = 0
    day = 1
    with open('./datas/work1.log', 'wt', encoding='utf-8') as f:
        while karma < MAX_SCORE:
            try:
                karma += one_day()
            except LiveException as e:
                print(f"Неудачный день {day}: {e}")
                f.write(f"Неудачный день {day}: {e}\n")
            day += 1
    print(f"Вы достигли кармы в {karma} за {day} дней!")


if __name__ == '__main__':
    game()
