"""
Задача 4. Класс с контролем цены и количества.

Создайте класс Product с атрибутами name, price, и quantity.
price должен быть положительным числом, а quantity неотрицательным целым числом.
При попытке установить price или quantity, должен производиться контроль значений.
"""
from descs.numb import RangeValidator


class Product:
    price = RangeValidator(num_min=0, value_type=(int, float))
    quantity = RangeValidator(num_min=0)

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"Продукт '{self.name}' (цена = {self.price}, количество = {self.quantity})"


if __name__ == '__main__':
    p = Product("DVD", 100, 10)
    t = Product("USB-HDD", 1000.0, 2)
    print(p)
    print(t)

    p.price = 12.0
    print(p)
