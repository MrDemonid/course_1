"""
Задание №4
� Создайте модуль с функцией внутри.
� Функция получает на вход загадку, список с возможными вариантами отгадок и количество попыток на угадывание.
� Программа возвращает номер попытки, с которой была отгадана загадка или ноль, если попытки исчерпаны.
"""

def run_quest(quest: str, answers: list[str], count) -> int:

    for i in range(len(answers)):
        answers[i] = answers[i].lower()
    print("Загадка: ", quest)
    for i in range(count):
        res = input("  введите ответ: ")
        if res.lower() in answers:
            return i+1
        print("  ответ неверный")
    return 0


if __name__ == '__main__':
    n = run_quest("Не лает, не кусает, а в дом не пускает", ["Сторож", "Охранник", "Замок"], 3)
    print(f"{n} attempts")
