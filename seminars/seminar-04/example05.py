"""
Задание №5
✔ Функция принимает на вход три списка одинаковой длины:
✔ имена str,
✔ ставка int,
✔ премия str с указанием процентов вида «10.25%».
✔ Вернуть словарь с именем в качестве ключа и суммой премии в качестве значения.
✔ Сумма рассчитывается как ставка умноженная на процент премии.
"""


def str_to_percent(lst: list[str]):
    res = []
    for s in lst:
        if s.endswith('%'):
            # res.append(s.split('%')[0])
            res.append(s.strip('%'))
        else:
            res.append(s)
    return res


def calc_bonus(names: list[str], amount: list[int], bonus: list[str]):
    b = str_to_percent(bonus)
    return [{names[i]: amount[i] * (float(b[i]) / 100.0)} for i in range(len(names))]


def calc_bonus2(names: list[str], amount: list[int], bonus: list[str]):
    """ Более затратный вариант, но тоже работает """
    return [{n: a * (float(b[:-1]) / 100)} for n, a, b in zip(names, amount, bonus)]


n = ["Иван", "Сергей", "Анна"]
a = [129, 89, 101]
b = ['12.4%', '8.5%', '9.8%']

print(calc_bonus(n, a, b))
print(calc_bonus2(n, a, b))
