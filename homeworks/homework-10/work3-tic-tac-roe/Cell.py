
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
        return f"{self.__class__.__name__} [{self.symbol}]"

