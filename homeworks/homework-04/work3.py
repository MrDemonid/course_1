"""
Задача 3. Число наоборот
Пользователь вводит два числа: N и K. Напишите программу, которая заменяет
каждое число на число, которое получается из исходного записью его цифр в
обратном порядке, затем складывает их, снова переворачивает и выводит
ответ на экран.
Пример:
Введите первое число: 102
Введите второе число: 123
Первое число наоборот: 201
Второе число наоборот: 321
Сумма: 522
Сумма наоборот: 225
"""

def reverse_number(n: int):
    d = []
    while n > 0:
        d.append(n % 10)
        n //= 10
    res = 0
    for digit in d:
        res = (res * 10 + digit)
    return res


n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))

r1 = reverse_number(n1)
r2 = reverse_number(n2)

print(f"n1 = {n1}, reverse = {r1};   n2 = {n2}, reverse = {r2}")

summ = reverse_number(r1 + r2)
print(f"sum = {(r1+r2)}, reverse sum = {summ}")
