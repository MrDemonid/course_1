"""
Задание №6.
Доработайте классы исключения так, чтобы они выдали подробную информацию об ошибках.
Передавайте необходимые данные из основного кода проекта.
"""
"""
Да у меня итак выдают всё подробно.
"""
import copy
import json
import os.path

from example03 import LevelError
from example03 import AccessError


class User:
    def __init__(self, idn, name, level=1):
        self.idn = idn
        self.name = name
        self.level = level

    @property
    def idn(self):
        return self._idn

    @property
    def name(self):
        return self._name

    @property
    def level(self):
        return self._level

    @idn.setter
    def idn(self, value):
        if not value is None:
            self._idn = value
        else:
            raise ValueError(f"Значение идентификатора не может быть пустым!")

    @name.setter
    def name(self, value):
        if not value is None and len(value) > 0:
            self._name = value
        else:
            raise ValueError(f"Некорректное значение '{value}' для имени")

    @level.setter
    def level(self, value):
        if (not value is None) and isinstance(value, int):
            if 1 <= value <= 7:
                self._level = value
            else:
                raise ValueError(f"Значение уровня '{value}' выходит за диапазон 1..7")
        else:
            raise TypeError(f"Значение уровня должно быть целым числом!")

    def __eq__(self, other):
        if isinstance(other, User):
            return self.idn == other.idn and self.name == other.name
        return NotImplemented

    def __hash__(self):
        return hash((self.idn, self.name))

    def __str__(self):
        return f"Юзер [id = {self.idn}, name = {self.name}, level = {self.level}"

    def __repr__(self):
        return f"User({self.idn}, {self.name}, {self.level})"


class Project:
    def __init__(self, fn):
        if fn is None or len(fn) == 0:
            raise ValueError("Неверное имя файла JSON")
        self.fn = fn
        self.user = None

    def enter_system(self):
        name = input("Введите имя пользователя: ")
        idn = input("Введите идентификатор: ")
        t = User(idn, name)
        for usr in self.load_users():
            if usr == t:
                try:
                    self.user = copy.deepcopy(usr)
                    print(f"Вход совершил: {self.user}")
                except Exception as e:
                    print(f"Ошибка входа: {e}")
                return
        raise AccessError(f"Пользователя с id = '{idn}' не существует!")

    def add_user(self, user: User):
        """
        Добавление нового пользователя.
        Уровень доступа должен быть меньше или равен уровню доступа текущего пользователя.
        """
        if user.level > self.user.level:
            raise LevelError(f"Вы не можете добавить пользователя с уровнем доступа выше вашего!")
        users = self.load_users()
        users.add(user)
        self.save_users(users)

    def load_users(self):
        """ Чтение множества User из файла JSON"""
        res = dict[str, dict[str, str]]
        if os.path.exists(self.fn):
            with open(self.fn, 'r', encoding='utf-8') as f:
                line = f.readlines()
                if len(line) > 0:
                    res = json.loads("".join(line))
        # print(res)
        # конвертируем в Users's
        users = set()
        for level, d in res.items():
            for idn, name in d.items():
                try:
                    users.add(User(idn, name, int(level)))
                except ValueError as e:
                    print(f"Ошибка: {e}")
                except TypeError as e:
                    print(f"Ошибка: {e}")
        return users

    def save_users(self, users: set[User]):
        # преобразуем в словарь
        persons = dict()
        for u in users:
            level = str(u.level)
            l: dict = persons.setdefault(level, dict())
            l[u.idn] = u.name
            persons[level] = l
        # print(persons)
        if len(persons) == 0:
            return
        # и сохраняем обратно в файл
        with open(self.fn, 'w', encoding='utf-8') as f:
            json.dump(persons, f, indent=2, ensure_ascii=False, sort_keys=True)


def new_user():
    """ Ввод данных для нового юзера. """
    while True:
        name = input("Введите имя: ")
        if 'exit' == name.lower():
            return None
        idn = input("Введите идентификатор: ")
        level = (input("Введите уровень доступа (1 - 7): "))
        try:
            return User(idn, name, int(level))
        except ValueError as e:
            print(f"Ошибка ввода: {e}\nПопробуйте снова.")
        except TypeError as e:
            print(f"Ошибка ввода type: {e}\nПопробуйте снова.")


if __name__ == '__main__':
    current = Project("./datas/ex2.json")
    try:
        current.enter_system()
        u = new_user()
        if u is None:
            exit(0xBABA)
        current.add_user(u)

    except Exception as e:
        print(e)

