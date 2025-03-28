from Cell import Cell


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

    def is_empty(self):
        return any([c.is_empty() for c in self.cells])

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


if __name__ == '__main__':
    b = Board(3)
    print(b.is_empty())
    b.change_cell(1, 'x')
    b.change_cell(2, 'x')
    b.change_cell(3, 'x')
    b.change_cell(4, 'x')
    b.change_cell(5, 'x')
    b.change_cell(6, 'x')
    b.change_cell(7, 'x')
    b.change_cell(8, 'x')
    b.change_cell(9, 'x')
    print(b.is_empty())