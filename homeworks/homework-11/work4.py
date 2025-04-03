"""
Задача 4. Стек.

В программировании нередко необходимо создавать свои собственные
структуры данных на основе уже существующих. Одной из таких базовых
структур является стек.
Стек — это абстрактный тип данных, представляющий собой список элементов,
организованных по принципу LIFO (англ. last in — first out, «последним пришёл —
первым вышел»).
Простой пример:
    стек из книг на столе. Единственной книгой, обложка которой
    видна, является самая верхняя. Чтобы получить доступ, например, к третьей
    снизу книге, нам нужно убрать все книги, лежащие сверху, одну за другой.

Напишите класс, который реализует стек и его возможности (достаточно будет
добавления и удаления элемента).

После этого напишите ещё один класс — «Менеджер задач».
В менеджере задач можно выполнить команду «новая задача», в которую передаётся сама
задача (str) и её приоритет (int). Сам менеджер работает на основе стека (не
наследование). При выводе менеджера в консоль все задачи должны быть отсортированы
по следующему приоритету: чем меньше число, тем выше задача.

Вот пример основной программы:
manager = TaskManager()
manager.new_task("сделать уборку", 4)
manager.new_task("помыть посуду", 4)
manager.new_task("отдохнуть", 1)
manager.new_task("поесть", 2)
manager.new_task("сдать ДЗ", 2)
print(manager)

Результат:
1 — отдохнуть
2 — поесть; сдать ДЗ
4 — сделать уборку; помыть посуду

Дополнительно: реализуйте также удаление задач и подумайте, что делать с дубликатами.
"""
import copy


class Stack:
    def __init__(self):
        self._storage = []

    def is_empty(self):
        return len(self._storage) == 0

    def push(self, item):
        self._storage.insert(0, item)

    def find(self, item):
        """ Возвращает позицию элемента (от 1)"""
        for i, v in enumerate(self._storage, start=1):
            if v == item:
                return i
        return None

    def pop(self, index=None):
        """ Извлечение элемента из стека. По дефолту это последний пришедший. """
        if index is None and not self.is_empty():
            return self._storage.pop(0)
        if 0 < index <= len(self._storage):
            return self._storage.pop(index - 1)
        return None

    def __str__(self):
        return f"Содержимое стека:\n{'\n'.join([str(i) for i in self._storage])}"


class Manager:
    """ Менеджер задач """

    def __init__(self):
        self._tasks = dict()

    def add_task(self, level, text):
        """ Добавление новой задачи """
        self._tasks.setdefault(level, Stack())
        if self._tasks[level].find(text) is None:
            self._tasks[level].push(text)

    def del_task(self, text):
        """ Удаление задачи из всех стеков """
        for t in self._tasks.values():
            i = t.find(text)
            if not i is None:
                t.pop(i)

    def __str__(self):
        keys = sorted(self._tasks.keys())
        res = []
        for k in keys:
            st: Stack = copy.deepcopy(self._tasks[k])
            tasks = []
            while not st.is_empty():
                tasks.append(st.pop())
            res.append(f"{k}: {'; '.join(tasks)}")
        return '\n'.join(res)


if __name__ == '__main__':
    manager = Manager()
    manager.add_task(4, "сделать уборку")
    manager.add_task(4, "помыть посуду")
    manager.add_task(1, "отдохнуть")
    manager.add_task(2, "поесть")
    manager.add_task(2, "сдать дз")
    manager.add_task(2, "сделать уборку")
    manager.add_task(2, "поесть")  # пробуем добавить дубликат
    # Печать списка задач
    print(manager)
    # Удаление задачи и повторный вывод
    manager.del_task("поесть")
    manager.del_task("сделать уборку")  # должно удалиться во всех уровнях привилегий
    print("\nПосле удаления задачи:")
    print(manager)
