"""
Задание 1. Функцию группового переименования файлов.

Напишите функцию группового переименования файлов. Она должна:
1. принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
2. принимать параметр количество цифр в порядковом номере.
3. принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
4. принимать параметр расширение конечного файла.
5. принимать диапазон сохраняемого оригинального имени.

Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла.
К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик
файлов и расширение.
"""

import os


def foo(directory, end_name, len_num, ext_src, ext_dst, start_range: tuple[int, int]):
    if os.path.isdir(directory) and len_num > 0 and ext_src and ext_dst and len(start_range) > 1:
        if end_name is None:
            end_name = ''
        lst = [f for f in os.listdir(directory) if f.endswith(ext_src)]
        for count, f in enumerate(lst, start=1):
            dst = os.path.splitext(f)
            if start_range:
                s, e, *_ = start_range
                dst = dst[0][s:(s + e + 1)]
            if not ext_dst.startswith('.'):
                ext_dst = '.' + ext_dst
            dst += end_name + f"{count}".zfill(len_num) + ext_dst
            print(dst)
            os.rename(os.path.join(directory, f), os.path.join(directory, dst))


if __name__ == '__main__':
    foo('./dir-01', '-', 3, 'py', 'txt', (0, 3))
