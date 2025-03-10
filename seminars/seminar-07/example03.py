"""
Задание №3
✔ Напишите функцию, которая открывает на чтение созданные в прошлых задачах файлы с числами и именами.
✔ Перемножьте пары чисел. В новый файл сохраните имя и произведение:
✔ если результат умножения отрицательный, сохраните имя записанное строчными буквами и произведение по модулю
✔ если результат умножения положительный, сохраните имя прописными буквами и произведение округлённое до целого.
✔ В результирующем файле должно быть столько же строк, сколько в более длинном файле.
✔ При достижении конца более короткого файла, возвращайтесь в его начало.
"""


def _mul_nums(src: str):
    s = src.split('|')
    if len(s) != 2:
        return None
    n = int(s[0])
    f = float(s[1])
    return n * f


def convert_files(nums_file, names_file, dest_file):
    with (open(nums_file, 'r', encoding='utf-8') as f1,
          open(names_file, 'r', encoding='utf-8') as f2,
          open(dest_file, 'w', encoding='utf-8') as dst):
        nums_src = f1.readlines()
        names_src = f2.readlines()
        for index in range(max(len(nums_src), len(names_src))):
            s = names_src[index % len(names_src)]
            n = _mul_nums(nums_src[index % len(nums_src)])
            if n is None:
                continue
            if n >= 0:
                dst.write(f"{(s[:-1].upper())}|{(int(n))}\n")
            elif n < 0:
                dst.write(f"{s[:-1].lower()}|{abs(n):.2f}\n")


if __name__ == '__main__':
    convert_files('./datas/numbers.txt', './datas/names.txt', './datas/combi3.txt')
