class Magic:
    """ Базовый класс магии """

    def __init__(self, name):
        self.name = name
        self.mixtures = dict()  # словарь возможных соединений компонентов

    def find_mixture(self, other):
        """ Поиск варианта соединения с заданным классом компонента """
        cls = other.__class__.__name__
        for k, v in self.mixtures.items():
            if k == cls:
                return v()
        return None

    def __add__(self, other):
        return self.find_mixture(other)

    def __str__(self):
        return f"{self.name}"

