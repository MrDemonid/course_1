"""
Задание №6
Напишите программу банкомат.
✔ Начальная сумма равна нулю
✔ Допустимые действия: пополнить, снять, выйти
✔ Сумма пополнения и снятия кратны 50 у.е.
✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
✔ Нельзя снять больше, чем на счёте
✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
операцией, даже ошибочной
✔ Любое действие выводит сумму денег
"""

import decimal
from View.menu import *
from View.ansi import *
from View.menucmd import *

ALIGN = 50                                  # кратность суммы для операций пополнения и снятия
PERCENT_FOR_WITHDRAWAL = 1.5                # процент за снятие наличных
MIN_CASH = 30                               # минимум за снятие наличных
MAX_CASH = 600                              # максимум за снятие наличных
LIMIT_TO_FREE = 5000000                     # максимум, до которого не берется налог на богатство
PERCENT_FOR_LIMIT = 10                      # процент налога на богатство


count_operations = 0                        # счетчик операций
total_cash: decimal = 0                     # средства юзера


def check_align(balance):
    if balance % ALIGN == 0:
        return True
    return False

'''
    Для каждой третьей операции начисляем 3%
'''
def check_bonus(balance: decimal) -> decimal:
    global count_operations
    count_operations += 1
    if count_operations % 3 == 0:
        percents = balance * (decimal.Decimal(PERCENT_FOR_WITHDRAWAL) / decimal.Decimal(100))
        print(f"\n  -- бонус на каждую третью операцию: {percents}")
        return balance + percents
    return balance

'''
    Снятие налога на богатство
'''
def check_limit(balance: decimal) -> decimal:
    if balance > decimal.Decimal(LIMIT_TO_FREE):
        percents = balance * (decimal.Decimal(PERCENT_FOR_LIMIT) / decimal.Decimal(100))
        print(f"  -- снятие налога на богатство: {percents}")
        return balance - percents
    return balance

'''
    Вычисляет снимаемую сумму, с учетом процентов
    Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
'''
def get_out_cash(out: decimal) -> decimal:
    percent = out * (decimal.Decimal(PERCENT_FOR_WITHDRAWAL) / decimal.Decimal(100))
    if percent < decimal.Decimal(MIN_CASH):
        percent = decimal.Decimal(MIN_CASH)
    elif percent > decimal.Decimal(MAX_CASH):
        percent = decimal.Decimal(MAX_CASH)
    print(f"  -- процент за снятие: {percent}")
    return percent + out

'''
    Пополнение баланса
'''
def top_up(balance: decimal) -> decimal:
    cls()
    print(ANSI_CYAN_BACKGROUND, ANSI_BLACK, "Пополнение баланса", ANSI_BLACK_BACKGROUND, ANSI_WHITE, end = "")
    print(f"\t(Текущий баланс: {balance})")
    balance = check_limit(balance)
    summ = int(input("\n  Введите сумму пополнения, кратную 50: "))
    if summ > 0 and check_align(summ):
        balance += decimal.Decimal(summ)
        balance = check_bonus(balance)
        print(f"  Баланс пополнен на {summ}, всего на счету: {balance}")
    else:
        print(ANSI_RED, f"\n  Сумма пополнения должна быть кратна {ALIGN}", ANSI_WHITE)
    return balance


'''
    Снятие с баланса
'''
def down_up(balance: decimal) -> decimal:
    cls()
    print(ANSI_CYAN_BACKGROUND, ANSI_BLACK, "Снятие с баланса", ANSI_BLACK_BACKGROUND, ANSI_WHITE, end = "")
    print(f"\t(Текущий баланс: {balance})")
    balance = check_limit(balance)
    summ = int(input("\n  Введите сумму снятия, кратную 50: "))
    if summ > 0 and check_align(summ):
        out = get_out_cash(decimal.Decimal(summ))
        if balance >= out:
            balance -= out
            balance = check_bonus(balance)
            print(f"  Снято: {summ}, списано: {out}, остаток: {balance}")
    else:
        print(ANSI_RED, f"\n  Сумма пополнения должна быть кратна {ALIGN}", ANSI_WHITE)
    return balance


'''
    Создаем меню и запускаем основной цикл приложения
'''
m = Menu("Банкомат. v 1.0", [
    MenuItem(CASH_IN_OP, "Пополнить"),
    MenuItem(CASH_OUT_OP, "Снять")
])

while True:
    n = m.run()
    if n == CASH_IN_OP:
        total_cash = top_up(total_cash)
    if n == CASH_OUT_OP:
        total_cash = down_up(total_cash)
    elif n == 0:
        break
