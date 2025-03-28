from random import randint
from Board import Board
from Player import Player


class Game:
    def __init__(self, p1: Player, p2: Player, size=3):
        self.players = [p1, p2]
        self.board = Board(size)
        self.current = 0

    def init(self):
        self.current = randint(0, 1)
        self.board.reset_board()

    def get_current_player(self):
        return self.players[self.current]

    def next_player(self):
        self.current ^= 1

    def step(self):
        """ Ход одного игрока """
        p = self.get_current_player()
        while self.board.is_empty():
            cell = p.step()
            if self.board.change_cell(cell, p.get_symbol()):
                return self.board.check_game()
            else:
                print("Нельзя ходить в занятую клетку. Повторите.")
        return False

    def game(self):
        """ Игра """
        while True:
            self.init()
            while True:
                self.board.show()
                if self.step():
                    print(f"{self.get_current_player().name} выиграл!")
                    break
                if not self.board.is_empty():
                    print("Ничья!")
                    break
                self.next_player()

            self.board.show()
            c = input("Хотите начать новую игру (Y/N)?")
            if c.upper() != 'Y' and c.upper() != 'Д':
                break
