"""
Задание №3.
Добавьте к задачам 1 и 2 строки документации для классов.
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


t = Archive(1, "string 1")
print(t.__doc__)
print(t.__dict__)
print(Archive.__dict__)
