"""
Задача 3. Планирование задач.

Напишите функцию, которая принимает количество дней от текущей даты и
возвращает дату, которая наступит через указанное количество дней.
Дополнительно, выведите эту дату в формате YYYY-MM-DD.
"""
from datetime import datetime, timedelta
import argparse


def calc_date(delta):
    cur = datetime.now()
    res = cur + timedelta(days=delta)
    return res


if __name__ == '__main__':
    # парсим ком. строку, на предмет параметра с дельтой дней (по дефолту 30)
    p = argparse.ArgumentParser(description="Program for calc of delta date.")
    p.add_argument("-d", metavar="days", type=int, default=30, help="number of days delta")
    args = p.parse_args()

    cur_date = datetime.now().strftime('%d.%m.%Y')          # текущая дата
    next_date = calc_date(args.d).strftime('%d.%m.%Y')      # получаем заданную дату
    print(f"{cur_date} + {args.d} = {next_date}")
