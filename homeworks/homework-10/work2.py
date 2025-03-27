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
