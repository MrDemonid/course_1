"""
Задание 1. Тестирование класса с использованием pytest.

Напишите класс BankAccount, который управляет балансом счета. Он должен поддерживать следующие методы:
    ● deposit(amount): добавляет указанную сумму к балансу.
    ● withdraw(amount): снимает указанную сумму с баланса, если достаточно средств.
    ● get_balance(): возвращает текущий баланс счета.

При попытке снять больше средств, чем доступно на счете, должно
выбрасываться исключение InsufficientFundsError.
Напишите как минимум 5 тестов для проверки работы классов и его методов.
"""


class InsufficientFundsError(Exception):
    def __init__(self):
        super().__init__("Недостаточно средств на счете!")


class BankAccount:

    def __init__(self, balance=0):
        self._balance = balance

    def deposit(self, amount):
        if not isinstance(amount, (int, float)):
            raise TypeError("Добавить можно только число!")
        if amount <= 0:
            raise ValueError("Добавить можно только положительное число!")
        self._balance += amount

    def withdraw(self, amount):
        if not isinstance(amount, (int, float)):
            raise TypeError("Снять можно только число!")
        if amount <= 0:
            raise ValueError("Снять можно только положительное число!")
        if amount > self._balance:
            raise InsufficientFundsError()
        self._balance -= amount

    def get_balance(self):
        return self._balance


import pytest

@pytest.fixture
def create_account():
    return BankAccount(10)

# проверка правильной инициализации объекта
def test_create(create_account):
    assert create_account.get_balance() == 10, 'Должно быть 10'

# проверка добавления средств
def test_deposit(create_account):
    create_account.deposit(4)
    assert create_account.get_balance() == 14, 'Депозит должен быть равен 14'

# проверка некорректного добавления средств
def test_deposit_type(create_account):
    with pytest.raises(TypeError, match=r'Добавить можно только число!'):
        create_account.deposit('as')

def test_deposit_value(create_account):
    with pytest.raises(ValueError, match=r'Добавить можно только положительное число!'):
        create_account.deposit(0)

# проверка снятия средств
def test_withdraw(create_account):
    create_account.withdraw(7)
    assert create_account.get_balance() == 3, 'Должно быть 3'

# проверка некорректного снятия средств
def test_withdraw_val(create_account):
    with pytest.raises(ValueError, match=r'Снять можно только положительное число!'):
        create_account.withdraw(0)

# проверка снятия средств больше доступного
def test_withdraw_exc(create_account):
    with pytest.raises(InsufficientFundsError, match=r'Недостаточно средств на счете!'):
        create_account.withdraw(12)



if __name__ == '__main__':
    pytest.main(['-v'])
