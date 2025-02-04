"""
Задача 4. Яма
Представьте, что вы разрабатываете компьютерную игру с текстовой графикой.
Вам поручили создать генератор ландшафта. Напишите программу, которая
получает на вход число N и выводит на экран числа в виде ямы
"""


"""
    Ввод числа. 
"""
def input_number(message: str):
    while True:
        try:
            num = int(input(f"{message}: "))
            if num < 0:
                quit()
            return num
        except KeyboardInterrupt:
            print("Ошибка ввода, попробуйте снова.")
            continue
        except ValueError:
            print("Неверные данные, попробуйте снова.")
            continue
        except EOFError:
            print("Неожиданный конец ввода, попробуйте снова.")
            continue


"""
    Рисует одну линию ямы
"""
def draw_pit(depth: int):
    start_symbol = depth
    while depth > 0:
        for i in range(start_symbol, depth - 1, -1):
            print(i, end="")
        print("." * (depth - 1) * 2, end="")
        for i in range(depth, start_symbol + 1):
            print(i, end="")
        print()
        depth -= 1


"""
    Основной код
"""
height = input_number("Введите глубину ямы")
draw_pit(height)
