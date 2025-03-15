"""
Задание №1.

Вспоминаем задачу 3 из прошлого семинара.
Мы сформировали текстовый файл с псевдо именами и произведением чисел.
Напишите функцию, которая создаёт из созданного ранее файла новый с данными в формате JSON.
Имена пишите с большой буквы.
Каждую пару сохраняйте с новой строки.
"""
import os.path
import json


def combi_to_json(fn):
    d = dict()
    with open(fn, 'r', encoding='utf-8') as f:
        for s in f:
            p = s[:-1].split('|')
            d[p[0].title()] = float(p[1])
    # строим новое имя файла
    t = os.path.split(fn)[1]
    name = os.path.join('./datas', os.path.splitext(t)[0] + '.json')
    with open(name, 'w', encoding='utf-8') as f:
        json.dump(d, f, indent=2, ensure_ascii=False)


if __name__ == '__main__':
    combi_to_json('../seminar-07/datas/combi3.txt')
