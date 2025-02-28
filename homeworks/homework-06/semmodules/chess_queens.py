"""
Задача 5. Модуль для проверки ферзей.

Добавьте в пакет, созданный на семинаре шахматный модуль. Внутри него
напишите код, решающий задачу о 8 ферзях. Известно, что на доске 8×8 можно
расставить 8 ферзей так, чтобы они не били друг друга. Вам дана расстановка 8
ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
Программа получает на вход восемь пар чисел, каждое число от 1 до 8 -
координаты 8 ферзей. Если ферзи не бьют друг друга верните истину, а если бьют
- ложь.
"""

__all__ = ['check_queens']

__IS_DEBUG = False

def __check_intersect(pos1: tuple[int, int], pos2: tuple[int, int]):
    """
    Проверка пары ферзей на возможность бить друг-друга

    Вернет True, если ферзи могут бить друг друга.
    """
    # проверяем горизонталь и вертикаль
    if pos1[0] == pos2[0] or pos1[1] == pos2[1]:
        if __IS_DEBUG:
            print(f"  -- intersect: ({pos1[0]}, {pos1[1]}) to ({pos2[0]}, {pos2[1]})")
        return True
    # проверяем диагонали
    dx = abs(pos1[0] - pos2[0])
    dy = abs(pos1[1] - pos2[1])
    if dx == dy:
        if __IS_DEBUG:
            print(f"  -- diagonal intersect: ({pos1[0]}, {pos1[1]}) to ({pos2[0]}, {pos2[1]})")
        return True
    return False


def check_queens(pos: list[tuple[int, int]]):
    """
    Проверка ферзей.

    Если есть пара, которая может бить друг-друга, то вернет False.
    Иначе вернет True.

    На входе: список координат (кортежей)
    """
    for i in range(0, len(pos)-1):
        for j in range(i+1, len(pos)):
            if __check_intersect(pos[i], pos[j]):
                return False
    return True


__intersect = [(1, 6), (2, 3), (3, 5), (4, 7), (5, 1), (6, 5), (7, 2), (8, 8)]
__no_intersect = [(1, 6), (2, 3), (3, 5), (4, 7), (5, 1), (6, 4), (7, 2), (8, 8)]


if __name__ == '__main__':
    __IS_DEBUG = True
    print(check_queens(__intersect))
    print(check_queens(__no_intersect))
