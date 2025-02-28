"""
Задание №7
� Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY
� Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна.
� Для простоты договоримся, что год может быть в диапазоне [1, 9999].
� Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь.
� Проверку года на високосность вынести в отдельную защищённую функцию.
"""

import re

__all__ = ['is_valid_date']

_MIN_YEAR = 1
_MAX_YEAR = 9999


def __str_to_date(s):
    """ Преобразует строку в числа даты. Допускается запись даты через точку, дефис или наклонную черту. """
    # match = re.match(r"(\d{1,2})[./-](\d{1,2})[./-](\d{4})", s) # вариант, допускающий номера дней и месяца в одну цифру
    match = re.match(r"(\d{2})[./-](\d{2})[./-](\d{4})", s)  # вариант для привычного формата даты
    if match:
        return map(int, match.groups())
    return 0, 0, 0


# def __str_to_date(s: list[str]):
#     try:
#         return map(int, s)
#     except ValueError:
#         return 0, 0, 0


def _is_leap_year(year):
    """ Проверка на високосность """
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def _get_days_in_month(year, month):
    """ Возвращает количество дней в месяце. """
    if month == 2:
        if _is_leap_year(year):
            return 29
        return 28
    if month in [4, 6, 9, 11]:
        return 30
    return 31


def is_valid_date(date: str) -> bool:
    """ Проверяет дату на корректность """
    day, mon, year = __str_to_date(date)

    if mon < 1 or mon > 12 or year < _MIN_YEAR or year > _MAX_YEAR:
        return False

    month_days = _get_days_in_month(year, mon)
    if day < 1 or day > month_days:
        return False

    return True


if __name__ == '__main__':
    """ Тесты """
    print(is_valid_date('12-12-1000'))
    print(is_valid_date('32.12.1999'))
    print(is_valid_date('29.02.2025'))
    print(is_valid_date('28.02.2025'))
