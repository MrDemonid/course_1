"""
Задание №5
� Добавьте в модуль с загадками функцию, которая хранит словарь списков.
� Ключ словаря - загадка, значение - список с отгадками.
� Функция в цикле вызывает загадывающую функцию, чтобы передать ей все свои загадки.
"""

_MAX_ATTEMPTS = 3

def _run_quest(quest: str, answers: list[str], count) -> int:

    for i in range(len(answers)):
        answers[i] = answers[i].lower()
    print("Загадка: ", quest)
    for i in range(count):
        res = input("  введите ответ: ")
        if res.lower() in answers:
            return i+1
        print("  ответ неверный")
    return 0


_quests = {"Не лает, не кусает, а в дом не пускает": ["Замок", "Охранник", "Сторож"],
           "Нет ушей, а слышит, нету рук, а пишет": ["Магнитофон", "Магнитола"]
           }

def do_quests():
    for k, v in _quests.items():
        n = _run_quest(k, v, _MAX_ATTEMPTS)
        if n > 0:
            print(f"Угадали с {n} попытки!")
        else:
            print(f"Не угадали, правильные ответы: {v}")
        print()


if __name__ == '__main__':
    do_quests()

