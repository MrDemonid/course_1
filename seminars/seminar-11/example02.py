"""
Задание №2.

Создайте класс Архив, который хранит пару свойств. Например, число и строку.
При нового экземпляра класса, старые данные из ранее созданных экземпляров
сохраняются в пару списков архивов
list-архивы также являются свойствами экземпляра
"""


class Archive:
    num_archives = []
    str_archives = []
    last_num = None
    last_str = None

    def __init__(self, n, s):
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
p = Archive(2, "string 2")
k = Archive(3, "string 3")
print(t)
print(k.str_archives)
