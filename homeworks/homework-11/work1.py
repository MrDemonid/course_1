"""
Задание 1. Матрицы.

Вы стажируетесь в лаборатории искусственного интеллекта, в ней вам
поручили разработать класс Matrix для обработки и анализа данных.
Ваш класс должен предоставлять функциональность для выполнения основных
операций с матрицами, таких как сложение, вычитание, умножение и транспонирование.
Это будет полезно для обработки и структурирования больших объёмов
данных, которые используются в обучении нейронных сетей.

Задача
    1. Создайте класс Matrix для работы с матрицами.
        Реализуйте методы:
            ○ сложения,
            ○ вычитания,
            ○ умножения,
            ○ транспонирования матрицы.
    2. Создайте несколько экземпляров класса Matrix и протестируйте реализованные операции.

Советы
    ● Методы сложения/вычитания/умножения должны получать параметром
        другую матрицу (объект класса Matrix) и выполнять указанное действие
        над своей и этой другой матрицей. Например, метод сложения должен
        получить параметром новую матрицу и сложить её со своей текущей.
    ● Метод транспонирования не должен ничего получать, он должен
        работать исключительно со своей матрицей.
    ● Транспонирование — это алгоритм, при котором строки матрицы
        меняются местами с её столбцами:
        [2 3 ] -> [ 2 4 ]
        [4 5 ]    [ 3 5 ]
        ----------------
        [ 2 6 ] -> [ 2 3 4 5 ]
        [ 3 7 ]    [ 6 7 8 9 ]
        [ 4 8 ]
        [ 5 9 ]
    ● Алгоритм транспонирования матрицы можно расписать следующим образом:
        1. Создать новую матрицу result с размерами, обратными размерам
            исходной матрицы. Количество строк новой матрицы равно
            количеству столбцов исходной, а количество столбцов новой
            матрицы равно количеству строк исходной.
        2. Пройтись по каждому элементу исходной матрицы. Для каждого
            элемента с индексами (i, j):
                1. Поместить значение этого элемента (i, j) в ячейку с
                    индексами (j, i) новой матрицы. То есть транспонирование
                    происходит с помощью обмена индексов местами.
                2. После завершения цикла новая матрица result будет
                    содержать транспонированную матрицу, которую можно вернуть.

Пример:
# Создание экземпляров класса Matrix
m1 = Matrix(2, 3)
m1.data = [[1, 2, 3], [4, 5, 6]]
m2 = Matrix(2, 3)
m2.data = [[7, 8, 9], [10, 11, 12]]

# Тестирование операций
print("Матрица 1:")
print(m1)
print("Матрица 2:")
print(m2)
print("Сложение матриц:")
print(m1.add(m2))
print("Вычитание матриц:")
print(m1.subtract(m2))
m3 = Matrix(3, 2)
m3.data = [[1, 2], [3, 4], [5, 6]]
print("Умножение матриц:")
print(m1.multiply(m3))
print("Транспонирование матрицы 1:")
print(m1.transpose())

Вывод
Матрица 1:
1 2 3
4 5 6
Матрица 2:
7 8 9
10 11 12
Сложение матриц:
8 10 12
14 16 18
Вычитание матриц:
-6 -6 -6
-6 -6 -6
Умножение матриц:
22 28
49 64
Транспонирование матрицы 1:
1 4
2 5
3 6
"""


class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.matrix = [[0 for _ in range(cols)] for _ in range(rows)]

    def _check_size(self, other):
        return self.rows == other.rows and self.cols == other.cols

    def __add__(self, other):
        if self._check_size(other):
            res = Matrix(self.rows, self.cols)
            for i in range(self.rows):
                for j in range(self.cols):
                    res.matrix[i][j] = self.matrix[i][j] + other.matrix[i][j]
            return res
        raise ValueError("Матрицы должны иметь одинаковый размер.")

    def __sub__(self, other):
        if self._check_size(other):
            res = Matrix(self.rows, self.cols)
            for i in range(self.rows):
                for j in range(self.cols):
                    res.matrix[i][j] = self.matrix[i][j] - other.matrix[i][j]
            return res
        raise ValueError("Матрицы должны иметь одинаковый размер.")

    def __mul__(self, other):
        if self.cols == other.rows:
            res = Matrix(self.rows, other.cols)
            for i in range(self.rows):
                for j in range(other.cols):
                    for k in range(self.cols):
                        res.matrix[i][j] += self.matrix[i][k] * other.matrix[k][j]
            return res
        raise ValueError("Матрицы не подходят по размерам")

    def __neg__(self):
        """ Транспортирование матрицы """
        res = Matrix(self.cols, self.rows)
        for i in range(self.rows):
            for j in range(self.cols):
                res.matrix[j][i] = self.matrix[i][j]
        return res

    def __str__(self):
        res = ''
        for i in self.matrix:
            s = ""
            for n in i:
                s += ' |' + str(n).rjust(4, ' ')
            res += s + ' |\n'

        return res
        # return "\n".join(["\t".join(map(str, row)) for row in self.matrix])


m1 = Matrix(2, 3)
m1.matrix = [[1, 2, 3], [4, 5, 6]]
m2 = Matrix(2, 3)
m2.matrix = [[7, 8, 9], [10, 11, 12]]
m3 = Matrix(3, 2)
m3.matrix = [[1, 2], [3, 4], [5, 6]]

print(f"Сложение: \n{m1 + m2}")
print(f"Вычитание: \n{m1 - m2}")
print(f"Умножение: \n{m1 * m3}")
print(f"Транспортирование: \n{-m1}")
