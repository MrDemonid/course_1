#
# Нарисовать в консоли ёлку спросив
# у пользователя количество рядов.
# Пример результата:
# Сколько рядов у ёлки? 5
#     *
#    ***
#   *****
#  *******
# *********
#

DRAW_SYMBOL = "*"
SPACE_SYMBOL = " "


def draw(columns):
    width = columns * 2 - 1
    for i in range(1, columns + 1):
        # spaces
        for j in range(i, width // 2 + 1):
            print(SPACE_SYMBOL, sep="", end="")
        for j in range(1, i * 2):
            print(DRAW_SYMBOL, sep="", end="")
        print()


height = int(input("Введите высоту ёлки: "))
if 0 < height < 64:
    draw(height)
