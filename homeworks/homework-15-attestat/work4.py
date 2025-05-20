"""
Задача 4. Опции и флаги.

Напишите скрипт, который принимает два аргумента командной строки: число и строку.
Добавьте следующие опции:
    ● --verbose, если этот флаг установлен, скрипт должен выводить
        дополнительную информацию о процессе.
    ● --repeat, если этот параметр установлен, он должен указывать,
        сколько раз повторить строку в выводе.
"""
import argparse


if __name__ == '__main__':
    p = argparse.ArgumentParser("Demo of argument's parser.")
    p.add_argument("number", metavar='N', type=int, help="Number parameter")
    p.add_argument("string", metavar='S', type=str, help="String parameter")
    p.add_argument("--verbose", "-v", action="store_true", help="Show extended information")
    p.add_argument("--repeat", "-r", metavar="count", type=int, default=1, help="Num of repeat of show string's")

    # args = p.parse_args("--verbose 12 Test -r 4".split())
    args = p.parse_args()

    if args.verbose:
        print(f"The arguments: {args}")

    print(f"Number: {args.number}, String: {args.string * args.repeat}")


else:
    print("Sorry! This module is not a library!")