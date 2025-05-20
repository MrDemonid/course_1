
import argparse


def quadratic_equations(a, b, c):
    d = b ** 2 - 4 * a * c
    if d > 0:
        return (-b + d ** 0.5) / (2 * a), (-b - d ** 0.5) / (2 * a)
    if d == 0:
        return -b / (2 * a)
    return None


parser = argparse.ArgumentParser(prog='myprog',
                                 description='My first argument parser',
                                 epilog='Calc average mean')

# задаем ключевые аргументы
parser.add_argument('-a', metavar='number', type=float, default=0, help='enter "a" for ax^2+bx+c=0')
parser.add_argument('-b', metavar='number', type=float, default=0, help='enter "b" for ax^2+bx+c=0')
parser.add_argument('-c', metavar='number', type=float, default=0, help='enter "c" for ax^2+bx+c=0')

# задаем позиционные аргументы
parser.add_argument('numbers',
                    metavar='N',            # то, что отобразится в справке как название параметра
                    type=float,             # тип параметра (-ов)
                    nargs='*',              # количество параметров (* - сколько угодно,
                                            #                        ? - один,
                                            #                        1..N - точное число, больше нуля),
                                            # которые нужно собрать в list
                    help='press some numbers')
# args = parser.parse_args()      # sys.argv

args = parser.parse_args("-a 2 -b 12 -c 4 12.2 14.5".split())

print(quadratic_equations(args.a, args.b, args.c))

print(f'В скрипт передано: {args}')
print(args.numbers[1])
print(args.a)
# > python ./example13.py -a 2 -b 12 -c 4 12.2 14.5