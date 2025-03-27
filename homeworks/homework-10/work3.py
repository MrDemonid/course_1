"""
Задача 3. Крестики-нолики.

Создайте программу, которая реализует игру «Крестики-нолики». Для этого напишите:

1. Класс, который будет описывать поле игры.
class Board:
    # Класс поля, который создаёт у себя экземпляры клетки.
    # Пусть класс хранит информацию о состоянии поля (это может быть список из девяти элементов).
    # Помимо этого, класс должен содержать методы:
    # «Изменить состояние клетки». Метод получает номер клетки и, если клетка не занята, меняет её
                                   состояние. Если состояние удалось изменить, метод возвращает True,
                                   иначе возвращается False.
    # «Проверить окончание игры». Метод не получает входящих данных, но возвращает True/False.
                                  True — если один из игроков победил, False — если победителя нет.
2. Класс, который будет описывать одну клетку поля:
class Cell:
    # Клетка, у которой есть значения:
        # занята она или нет;
        # номер клетки;
        # символ, который клетка хранит (пустая, крестик, нолик).
3. Класс, который описывает поведение игрока:
class Player:
    # У игрока может быть:
    # имя,
    # количество побед.
    # Класс должен содержать метод:
        # «Сделать ход». Метод ничего не принимает и возвращает ход игрока (номер клетки).
                         Введённый номер нужно обязательно проверить.
4. Класс, который управляет ходом игры:
class Game:
    # класс «Игры» содержит атрибуты:
    # состояние игры,
    # игроки,
    # поле.
    # А также методы:
        # Метод запуска одного хода игры. Получает одного из игроков, запрашивает у игрока номер клетки,
          изменяет поле, проверяет, выиграл ли игрок. Если игрок победил, возвращает True, иначе False.
        # Метод запуска одной игры. Очищает поле, запускает цикл с игрой, который завершается победой одного
          из игроков или ничьей. Если игра завершена, метод возвращает True, иначе False.
        # Основной метод запуска игр. В цикле запускает игры, запрашивая после каждой игры, хотят ли игроки
          продолжать играть. После каждой игры выводится текущий счёт игроков.
"""


class Cell:
    def __init__(self, number):
        self.number = number
        self.symbol = ' '

    def is_empty(self):
        return self.symbol == ' '

    def get_symbol(self):
        return self.symbol

    def set_symbol(self, symbol):
        self.symbol = symbol

    def get_number(self):
        return self.number

    def __str__(self):
        return f"{self.symbol}"


class Board:

    def __init__(self, size):
        self._size = size
        self.cells = [Cell(i) for i in range(1, size * size + 1)]
        self.__make_tables(size)  # готовим таблицу для определения состояния игры

    def __make_tables(self, size):
        """ Создает таблицу с номерами ячеек, для быстрой проверки на чей-то выигрыш"""
        self._table = []
        # горизонталь и вертикаль
        for y in range(size):
            hor = []
            ver = []
            for x in range(size):
                hor.append(y * size + x)
                ver.append(y + x * size)
            self._table.append(hor)
            self._table.append(ver)
        # диагонали
        d1 = []
        d2 = []
        for i in range(size):
            d1.append(i * size + i)
            d2.append((size - i - 1) * size + i)
        self._table.append(d1)
        self._table.append(d2)

    def reset_board(self):
        """ Очистка игрового поля """
        for cell in self.cells:
            cell.set_symbol(' ')

    def change_cell(self, cell_number, symbol):
        """ Изменяет состояние ячейки, если она не занята """
        if (0 < cell_number <= len(self.cells)) and (symbol == 'x' or symbol == 'o'):
            cell = self.cells[cell_number - 1]
            if cell.is_empty():
                cell.set_symbol(symbol)
                return True
        return False

    def check_game(self):
        """ Проверка, не выиграл ли один из игроков"""
        for line in self._table:
            pos = line[0]
            ch = self.cells[pos].get_symbol()
            cnt = 0
            if not self.cells[pos].is_empty():
                for i in line:
                    if self.cells[i].get_symbol() == ch:
                        cnt += 1
            if cnt == len(line):
                return True
        return False

    def show(self):
        """ Вывод доски в консоль """
        for y in range(self._size):
            print('+---+---+---+')
            n = []
            for x in range(self._size):
                n.append(self.cells[y*self._size+x].get_symbol())
            s = " | ".join(n)
            print(f"| {s} |")
        print('+---+---+---+')


b = Board(3)
b.change_cell(1, 'x')
b.change_cell(5, 'x')
b.change_cell(3, 'o')
b.show()