"""
Задача 4. Генерация паролей.
    Напишите программу, которая генерирует случайный пароль заданной длины,
состоящий из букв, цифр и специальных символов.
"""
import random
import string

length = 0
while length < 6:
    length = int(input("Введите длину пароля: "))


base = string.ascii_letters + string.digits + string.punctuation

while True:
    t = "".join([random.choice(base) for _ in range(length)])
    if not t.isalnum():
        break

print("password: ", t)
