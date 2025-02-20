"""
Задание 1. Апгрейд калькулятора
Степан использует калькулятор для расчёта суммы и разности чисел, но на
работе ему требуются не только обычные арифметические действия. Он ничего
не хочет делать вручную, поэтому решил немного расширить функционал
калькулятора.
Напишите программу, запрашивающую у пользователя число и действие,
которое нужно сделать с числом: вывести сумму его цифр, максимальную или
минимальную цифру. Каждое действие оформите в виде отдельной функции, а
основную программу зациклите.
Запрошенные числа должны передаваться в функции суммы, максимума и
минимума при помощи аргументов.
"""

def sum_digit(n: int):
    res = 0
    while n > 0:
        res += n % 10
        n //= 10
    return res

def max_digit(n: int):
    _max = 0
    while n > 0:
        k = n % 10
        n //= 10
        if k > _max:
            _max = k
    return _max

def min_digit(n: int):
    _min = n % 10
    while n > 0:
        k = n % 10
        n //= 10
        if k < _min:
            _min = k
    return _min

operations = [sum_digit, max_digit, min_digit]

while True:
    action = int(input("Action:\n    1 - summ of digits\n    2 - max digit\n    3 - min digit\n    0 - exit\n"))
    if action == 0:
        quit()
    if 0 < action <= len(operations):
        number = int(input("Enter number: "))
        func = operations[action-1]
        print(f"result: {func(number)}")
    else:
        print("Error: incorrect action! Must be in range 1..3.")
