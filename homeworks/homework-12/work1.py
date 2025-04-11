"""
Задание 1. Работа с данными студентов.

Создайте класс студента.
    ○ Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только
        букв. Если ФИО не соответствует условию, выведите:
            ФИО должно состоять только из букв и начинаться с заглавной буквы
    ○ Названия предметов должны загружаться из файла CSV при создании экземпляра.
        Другие предметы в экземпляре недопустимы. Если такого предмета нет, выведите:
            Предмет {Название предмета} не найден
    ○ Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до
        100). В противном случае выведите:
            Оценка должна быть целым числом от 2 до 5
            Результат теста должен быть целым числом от 0 до 100
    ○ Также экземпляр должен сообщать средний балл по тестам для каждого предмета и по
        оценкам всех предметов вместе взятых.
Вам предоставлен файл subjects.csv, содержащий предметы. Сейчас в файл записана
следующая информация.
    Математика,Физика,История,Литература
Создайте класс Student, который будет представлять студента и его успехи по
предметам. Класс должен иметь следующие методы:
Атрибуты класса:
    name (str): ФИО студента.
    subjects (dict): Словарь, который хранит предметы в
        качестве ключей и информацию об оценках и результатах тестов для каждого предмета в
        виде словаря.
Магические методы (Dunder-методы):
    __init__(self, name, subjects_file): Конструктор класса. Принимает имя студента
        и файл с предметами и их результатами. Инициализирует атрибуты name и subjects и
        вызывает метод load_subjects для загрузки предметов из файла.
    __setattr__(self, name, value): Дескриптор, который проверяет установку атрибута
        name. Убеждается, что name начинается с заглавной буквы и состоит только из букв.
    __getattr__(self, name): Позволяет получать значения атрибутов предметов (оценок
        и результатов тестов) по их именам.
    __str__(self): Возвращает строковое представление студента, включая имя и список
        предметов.
            Студент: Иван Иванов
            Предметы: Математика, История
Методы класса:
    load_subjects(self, subjects_file): Загружает предметы из файла CSV.
        Использует модуль csv для чтения данных из файла и добавляет предметы в атрибут
        subjects.
    add_grade(self, subject, grade): Добавляет оценку по заданному предмету.
        Убеждается, что оценка является целым числом от 2 до 5.
    add_test_score(self, subject, test_score): Добавляет результат теста по
        заданному предмету. Убеждается, что результат теста является целым числом от 0 до 100.
    get_average_test_score(self, subject): Возвращает средний балл по тестам для
        заданного предмета.
    get_average_grade(self): Возвращает средний балл по всем предметам.

Пример
На входе:
student = Student("Иван Иванов", "subjects.csv")
student.add_grade("Математика", 4)
student.add_test_score("Математика", 85)
student.add_grade("История", 5)
student.add_test_score("История", 92)
average_grade = student.get_average_grade()
print(f"Средний балл: {average_grade}")
average_test_score = student.get_average_test_score("Математика")
print(f"Средний результат по тестам по математике:
{average_test_score}")
print(student)

На выходе:
Средний балл: 4.5
Средний результат по тестам по математике: 85.0
Студент: Иван Иванов
Предметы: Математика, История
"""
import csv


class FIO:
    """ Дескриптор для ФИО """

    def __set_name__(self, owner, name):
        self.name = f"_{name}"

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise TypeError(f"Значение '{value}' должно быть строкой!")

        parts = value.strip().split()
        if not (1 <= len(parts) <= 3):
            raise ValueError("ФИО должно содержать от 1 до 3 слов!")

        for part in parts:
            if not (part.isalpha() and part[0].isupper() and part[1:].islower()):
                raise ValueError(
                    "Каждая часть ФИО должна начинаться с заглавной буквы и содержать только буквы кириллицы!")
        setattr(instance, self.name, value)


class Number:
    """ Дескриптор для целых чисел из заданного диапазона """

    def __init__(self, num_min: int = None, num_max: int = None):
        self._min = num_min
        self._max = num_max

    def __set_name__(self, owner, name):
        self.name = f"_{name}"

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError(f"Значение '{value}' должно быть целочисленным!")
        if not self._min is None and value < self._min:
            raise ValueError(f"Значение '{value}' должно быть больше или равно '{self._min}'")
        if not self._max is None and value > self._max:
            raise ValueError(f"Значение '{value}' должно быть меньше или равно '{self._max}'")
        setattr(instance, self.name, value)


class Student:
    name = FIO()
    grade = Number(2, 5)  # используется на этапе добавления оценки
    test = Number(0, 100)  # используется на этапе добавления баллов

    def __init__(self, name: str, subjects_file: str):
        self.name = name
        self.subjects = self.load_subjects(subjects_file)  # словарь словарей

    def load_subjects(self, fn) -> dict:
        res = dict()
        try:
            with open(fn, newline='', encoding='utf-8') as f:
                reader = csv.reader(f)
                for line in reader:
                    rows = [row.strip() for row in line]  # получаем список столбцов (названий предметов)
                    for row in rows:
                        res[row] = {'grades': [], 'tests': []}
            return res
        except FileNotFoundError:
            raise FileNotFoundError(f"Error: file '{fn}' not found!")

    def __getattr__(self, name):
        if name in self.subjects:
            return self.subjects[name]
        raise AttributeError(f"Предмет '{name}' не найден!")

    def __str__(self):
        return f"Студент: {self.name}\nПредметы: {", ".join(self.subjects.keys())}"

    def add_grade(self, subject, grade):
        try:
            self.grade = grade
            if subject in self.subjects:
                self.subjects[subject]['grades'].append(self.grade)
            else:
                print(f"Предмет '{subject}' не найден!")
        finally:
            return

    def add_test(self, subject, test):
        try:
            self.test = test
            if subject in self.subjects:
                self.subjects[subject]['tests'].append(self.test)
            else:
                print(f"Предмет '{subject}' не найден!")
        finally:
            return

    def get_average_grade(self):
        """ средняя оценка по всем предметам """
        all_values = [ball for n in self.subjects.values() for ball in n['grades']]
        divider = len(all_values) if len(all_values) > 0 else 1
        return sum(all_values) / divider

    def get_average_test(self, subject):
        """ средний балл по тестам заданного предмета """
        if subject in self.subjects:
            all_values = self.subjects[subject]['tests']
            divider = len(all_values) if len(all_values) > 0 else 1
            return sum(all_values) / divider


if __name__ == '__main__':
    student = Student("Иван Иванов", "subjects.csv")

    # Добавляем оценки и результаты тестов
    student.add_grade("Математика", 4)
    student.add_test("Математика", 85)
    student.add_grade("История", 5)
    student.add_test("История", 92)
    student.add_test("Математика", 89)

    # Получаем средний балл и результат по тестам
    average_grade = student.get_average_grade()
    print(f"Средний балл: {average_grade}")
    average_test = student.get_average_test("Математика")
    print(f"Средний результат по тестам по математике: {average_test}")
    # Выводим информацию о студенте
    print(student)
