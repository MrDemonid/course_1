"""
Задача 4. Счетчик Очков в Игрe.

Создайте класс GameScore для отслеживания очков игрока.
В этом классе должны быть методы для добавления и уменьшения очков.
Однако:
    ● Очки не могут быть отрицательными.
    ● Если игрок пытается добавить больше очков, чем 1000,
      должно быть выброшено исключение ScoreLimitExceededError.

Создайте пользовательское исключение ScoreLimitExceededError.
"""

class ScoreLimitExceededError(Exception):
    def __init__(self):
        super().__init__('Нельзя добавить больше чем 1000 очков!')


class GameScore:

    def __init__(self):
        self.score = 0

    def add_score(self, num: int):
        if num > 0:
            if num > 1000:
                raise ScoreLimitExceededError()
            self.score += num
        else:
            raise ValueError("Нельзя прибавить отрицательное кол-во очков!")

    def sub_score(self, num: int):
        if 0 < num <= self.score:
            self.score -= num
        else:
            raise ValueError("Нельзя вычесть отрицательное кол-во очков или больше существующего!")

    def __str__(self):
        return f"Очков: {self.score}"


def op(method, param):
    try:
        print(f"call {method.__name__}({param})", end=' = ')
        method(param)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    score = GameScore()
    op(score.add_score, 189)
    print(score)
    op(score.add_score, -2)
    print(score)
    op(score.add_score, 2000)
    print(score)
    op(score.sub_score, -2)
    print(score)
    op(score.sub_score, 100)
    print(score)
    op(score.sub_score, 200)
    print(score)
