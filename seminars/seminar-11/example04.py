"""
Задание №4.

Доработаем класс Архив из задачи 2.
Добавьте методы представления экземпляра для программиста и для пользователя.
"""


class Archive:
    """
    Archive - класс с архивированием данных при создании новых экземпляров.
    """
    num_archives = []
    str_archives = []
    last_num = None
    last_str = None

    def __init__(self, n, s):
        """
        Инициализация экземпляра класса. Сохраняет данных предыдущего экземпляра в архив.
        @papam n: число
        @param s: строка
        """

        self.n = n
        self.s = s
        if Archive.last_num is not None:
            Archive.num_archives.append(Archive.last_num)
        if Archive.last_str is not None:
            Archive.str_archives.append(Archive.last_str)
        Archive.last_num = n
        Archive.last_str = s

    def __str__(self):
        return f"Archive [n = {self.n}, s = {self.s}]"

    def __repr__(self):
        return f"Archive({self.n}, {self.s})"


t = Archive(1, "String 1")
p = Archive(2, "String 2")
k = Archive(3, "String 3")
d = [t, p, k]

print(t, p, k, sep="\n")
print(d)
