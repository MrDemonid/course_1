"""
Задание №2.

Напишите функцию, которая в бесконечном цикле запрашивает имя, личный идентификатор и уровень доступа (от 1 до 7).
После каждого ввода добавляйте новую информацию в JSON файл.
Пользователи группируются по уровню доступа.
Идентификатор пользователя выступает ключём для имени.
Убедитесь, что все идентификаторы уникальны независимо от уровня доступа.
При перезапуске функции уже записанные в файл данные должны сохраняться.
"""
import json
import os.path


def _input_datas():
    name = input("Введите имя: ")
    if 'exit' == name.lower():
        return None
    idn = input("Введите идентификатор: ")
    while True:
        level = (input("Введите уровень доступа (1 - 7): "))
        if '0' < level <= '7':
            break
    return [name, idn, level]


def _check_id(d: dict, idn):
    """ Проверка дубликата ID """
    if not d is None and len(d) > 0:
        return len({idn for key in d.keys() for el in d[key] if idn in el}) > 0
    return False


def add_user(file_name):
    while True:
        # ввод данных нового юзера
        data = _input_datas()
        if data is None:
            break
        name, idn, level = data

        # читаем данные из файла
        persons = dict()
        if os.path.exists(file_name):
            with open(file_name, 'r', encoding='utf-8') as f:
                res = f.readlines()
                if len(res) > 0:
                    persons = json.loads("".join(res))

        # добавляем юзера в текущий словарь
        if not _check_id(persons, idn):
            l: dict = persons.setdefault(level, dict())
            l[idn] = name.title()
            persons[level] = l
        else:
            print('-- user id is already defined!')

        # и сохраняем обратно в файл
        with open(file_name, 'w', encoding='utf-8') as f:
            json.dump(persons, f, indent=2, ensure_ascii=False, sort_keys=True)


if __name__ == '__main__':
    add_user('./datas/ex2.json')
