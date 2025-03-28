# 3. Класс, который описывает поведение игрока:
# class Player:
#     # У игрока может быть:
#     # имя,
#     # количество побед.
#     # Класс должен содержать метод:
#         # «Сделать ход». Метод ничего не принимает и возвращает ход игрока (номер клетки).
#                          Введённый номер нужно обязательно проверить.


class Player:
    def __init__(self, name, symbol, size):
        self.name = name
        self.symbol = symbol
        self.wins = 0
        self._size = size

    def get_symbol(self):
        return self.symbol

    def get_wins(self):
        return self.wins

    def set_wins(self):
        self.wins += 1

    def step(self):
        while 1:
            try:
                n = int(input(f"{self.name}: введите номер клетки для хода (1 - {self._size}): "))
                if 0 < n <= self._size:
                    return n
                raise ValueError
            except ValueError:
                print("Некорректный номер клетки. Повторите.")

    def __str__(self):
        return f"{self.__class__.__name__} [{self.name}: symbol = {self.symbol}, wins = {self.wins}]"


if __name__ == '__main__':
    p = Player("Ivan", 'x', 9)
    print(p)
    print(p.step())
