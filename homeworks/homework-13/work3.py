"""
Задача 3. Счастливое число.

Напишите программу, которая запрашивает у пользователя число до тех пор, пока
сумма этих чисел не станет больше либо равна 777.
Каждое введенное число при этом дозаписывается в файл.
Сделайте так, чтобы перед дозаписью программа с вероятностью 1 к 13 выбрасывала
пользователю случайное исключение и завершалась.

Пример 1:
    Введите число: 10
    Введите число: 500
    Введите число: 200
    Введите число: 67
    Вы успешно выполнили условие для выхода из порочного цикла!

Содержимое файла out_file.txt:
    10
    500
    200
    67

Пример 2:
    Введите число: 10
    Введите число: 500
    Вас постигла неудача!
Содержимое файла out_file.txt:
    10
"""
import random

MAX_SCORE = 777


class Game:
    def __init__(self, fn='./datas/work3_out_file.txt'):
        self.fn = fn

    def input_number(self) -> int:
        while 1:
            try:
                return int(input("Введите число: "))
            except ValueError as e:
                print(f"Ошибка: {e}. Попробуйте снова.")

    def open_log(self):
        with open(self.fn, 'wt', encoding='utf-8') as f:
            f.write("begin game\n")

    def add_log(self, num):
        with open(self.fn, 'at', encoding='utf-8') as f:
            f.write(f"{num}\n")

    def do_game(self):
        score = 0
        self.open_log()
        while score < MAX_SCORE:
            num = self.input_number()
            if random.randint(1, 13) == 1:
                raise Exception("Вас постигла неудача!")
            score += num
            self.add_log(num)

    def do_run(self):
        try:
            self.do_game()
        except Exception as e:
            print(f"{e}")


if __name__ == '__main__':
    game = Game()
    game.do_run()
