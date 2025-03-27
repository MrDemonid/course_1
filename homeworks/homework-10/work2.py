"""
Задача 2. Совместное проживание.

Чтобы понять, стоит ли ему жить с кем-то или лучше остаться в гордом одиночестве, Артём
решил провести необычное исследование. Для этого он реализовал модель человека и модель дома.
Человек может (должны быть такие методы):
    ● есть (+ сытость, − еда);
    ● работать (− сытость, + деньги);
    ● играть (− сытость);
    ● ходить в магазин за едой (+ еда, − деньги);
    ● прожить один день (выбирает одно действие согласно описанному ниже приоритету и выполняет его).
У человека есть (должны быть такие атрибуты):
    ● имя,
    ● степень сытости (изначально 50),
    ● дом.
В доме есть:
    ● холодильник с едой (изначально 50 еды),
    ● тумбочка с деньгами (изначально 0 денег).
Если сытость человека становится меньше нуля, человек умирает.
Логика действий человека определяется следующим образом:
    1. Генерируется число кубика от 1 до 6.
    2. Если сытость < 20, то нужно поесть.
    3. Иначе, если еды в доме < 10, то сходить в магазин.
    4. Иначе, если денег в доме < 50, то работать.
    5. Иначе, если кубик равен 1, то работать.
    6. Иначе, если кубик равен 2, то поесть.
    7. Иначе играть.
По такой логике эксперимента человеку надо прожить 365 дней.
Реализуйте такую программу и создайте двух людей, живущих в одном доме.
Проверьте работу программы несколько раз
"""
from random import randint


class House:
    def __init__(self):
        self.food = 50
        self.many = 0

    def get_food(self):
        return self.food

    def get_many(self):
        return self.many

    def inc_food(self):
        self.food += 1

    def give_food(self):
        if self.food > 0:
            self.food -= 1
            return True
        return False

    def inc_many(self):
        self.many += 1

    def give_many(self):
        if self.many > 0:
            self.many -= 1
            return True
        return False


class Person:
    def __init__(self, name, house):
        self.name = name
        self.hungry = 50
        self.house = house
        self._eats = 0
        self._plays = 0
        self._works = 0
        self._go_true = 0
        self._go_fail = 0


    def eat(self):
        if self.house.give_food():
            self._eats += 1
            self.hungry += 1
            return True
        return False

    def work(self):
        self.hungry -= 1
        self.house.many += 1
        self._works += 1

    def play(self):
        self.hungry -= 1
        self._plays += 1

    def go_store(self):
        if self.house.give_many():
            self.house.inc_food()
            self._go_true += 1
            return True
        self._go_fail += 1
        return False

    def check(self):
        if self.hungry >= 0:
            return True
        return False

    def get_total_actions(self):
        return self._eats + self._works + self._plays + self._go_true + self._go_fail

    def live_day(self):
        step = randint(1, 6)
        if self.hungry < 20:
            if not self.eat():
                print("Внимание! Нечего есть!")
        elif self.house.get_food() < 10:
            if not self.go_store():
                print("Внимание! Нет денег на покупку еды!")
        elif self.house.get_many() < 50:
            self.work()
        elif step == 1:
            self.work()
        elif step == 2:
            self.eat()
        else:
            self.play()
        return self.check()

    def __str__(self):
        return (f"{self.name}: hungry = {self.hungry}, "
                f"food = {self.house.get_food()}, "
                f"many = {self.house.get_many()}, "
                f"eats = {self._eats}, works = {self._works}, plays = {self._plays}, "
                f"go to store = {self._go_true}, goto fail = {self._go_fail}, "
                f"total actions = {self.get_total_actions()}"
                )


def simulate(p1: Person, p2: Person, days):
    while days > 0:
        if not p1.live_day() or not p2.live_day():
            return False
        days -= 1
    return True

def multi_test(count):
    while count > 0:
        h = House()
        p1 = Person("Ivan", h)
        p2 = Person("Elena", h)
        res = simulate(p1, p2, 365)
        print(("Выжили" if res else "Неудача"))
        print(p1)
        print(p2)
        count -= 1

multi_test(3)

# Выжили
# Ivan: hungry = 19, food = 10, many = 50, eats = 118, works = 121, plays = 28, go to store = 98, goto fail = 0, total actions = 365
# Elena: hungry = 19, food = 10, many = 50, eats = 118, works = 125, plays = 24, go to store = 98, goto fail = 0, total actions = 365
# Выжили
# Ivan: hungry = 20, food = 9, many = 49, eats = 119, works = 123, plays = 26, go to store = 97, goto fail = 0, total actions = 365
# Elena: hungry = 20, food = 9, many = 49, eats = 118, works = 122, plays = 26, go to store = 99, goto fail = 0, total actions = 365
# Выжили
# Ivan: hungry = 19, food = 10, many = 50, eats = 118, works = 123, plays = 26, go to store = 98, goto fail = 0, total actions = 365
# Elena: hungry = 19, food = 10, many = 50, eats = 118, works = 123, plays = 26, go to store = 98, goto fail = 0, total actions = 365

