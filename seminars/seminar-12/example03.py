"""
Задание №3.
Создайте класс-генератор.
Экземпляр класса должен генерировать факториал числа в диапазоне от start до stop с шагом step.
Если переданы два параметра, считаем step=1.
Если передан один параметр, также считаем start=1.
"""


class Factorial:
    def __init__(self, stop, *, start=1, step=1):
        self.start = start if start > 0 else 1
        self.stop = stop
        self.step = step
        self.current = 1
        self.do_start()

    def do_start(self):
        for i in range(1, self.start):
            self.current *= i

    def __iter__(self):
        return self

    def __next__(self):
        if self.start <= self.stop:
            res = self.current * self.start
            # start += skip
            for i in range(self.step):
                self.current *= self.start
                self.start += 1
            return res
        raise StopIteration


f = Factorial(12, step=2)
for n in f:
    print(f"{n = :_}")
