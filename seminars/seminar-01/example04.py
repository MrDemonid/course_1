'''
Пользователь вводит число от 1 до 999. Используя операции с числами
сообщите что введено: цифра, двузначное число или трёхзначное число.
Для цифры верните её квадрат, например 5 - 25
Для двузначного числа произведение цифр, например 30 - 0
Для трёхзначного числа его зеркальное отображение, например 520 - 25
Если число не из диапазона, запросите новое число.
Откажитесь от магических чисел
В коде должны быть один input и один print
'''


def input_num():
    while True:
        number = int(input("Введите число от 1 до 999: "))
        if 0 < number < 1000:
            return number
        print("Неверное число. Попробуйте в следующий раз.")


def num_to_digits(num):
    digs = list()
    while num > 0:
        digs.append(num % 10)
        num //= 10
    return digs


def show_number(num):
    digits = num_to_digits(num)
    if len(digits) == 1:
        return digits[0] * digits[0]
    elif len(digits) == 2:
        return digits[0] * digits[1]
    elif len(digits) == 3:
        return digits[0] * 100 + digits[1] * 10 + digits[2]
    return -1


print(f"Результат: {show_number(input_num())}")
