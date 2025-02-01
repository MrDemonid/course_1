# Задание 1. Рамка
# Напишите программу, которая рисует прямоугольную рамку с помощью
# символьной графики. Для вертикальных линий используйте символ
# вертикального штриха (|), а для горизонтальных — дефис (-). Пусть ширину и
# высоту рамки определяет пользователь.

MIN_WIDTH = 2
MIN_HEIGHT = 2
MAX_WIDTH = 120
MAX_HEIGHT = 50

"""
    Ввод ширины и высоты рамки
"""
def input_size():
    while True:
        try:
            print("Для выхода введите отрицательное значение.")
            in_width = int(input(f"Введите ширину рамки (от {MIN_WIDTH} до {MAX_WIDTH}): "))
            in_height = int(input(f"Введите высоту рамки (от {MIN_HEIGHT} до {MAX_HEIGHT}): "))
            if in_width < 0 or in_height < 0:
                quit()
            if MIN_WIDTH <= in_width <= MAX_WIDTH and MIN_HEIGHT <= in_height <= MAX_HEIGHT:
                return [in_width, in_height]

        except KeyboardInterrupt:
            print("Ошибка ввода, попробуйте снова.")
            continue
        except ValueError:
            print("Неверные данные, попробуйте снова.")
            continue
        except EOFError:
            print("Неожиданный конец ввода, попробуйте снова.")
            continue



'''
    Отрисовка одной горизонтальной линии.
'''
def draw_hor_line(width, left_corner, symbol, right_corner):
    if width >= 2:
        print(left_corner, symbol * (width-2), right_corner, sep="")

'''
    Отрисовка рамки.
'''
def draw_border(width, height):
    if width >= 2 and height >= 2:
        height -= 2
        if height >= 0:
            draw_hor_line(width, "+", "-", "+")
            while height > 0:
                draw_hor_line(width, "|", " ", "|")
                height -= 1
            draw_hor_line(width, "+", "-", "+")


"""
    Собственно программа.
"""
border_width, border_height = input_size()
draw_border(border_width, border_height)
