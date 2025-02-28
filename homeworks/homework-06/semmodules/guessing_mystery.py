"""
Задание №6
� Добавьте в модуль с загадками функцию, которая принимает на вход строку (текст загадки) и число (номер попытки, с которой она угадана).
� Функция формирует словарь с информацией о результатах отгадывания.
� Для хранения используйте защищённый словарь уровня модуля.
� Отдельно напишите функцию, которая выводит результаты угадывания из защищённого словаря в удобном для чтения виде.
� Для формирования результатов используйте генераторное выражение.
"""

__all__ = ['do_quests', 'show_results']

_MAX_ATTEMPTS = 3  # макс. кол-во попыток

# Вопросы и ответы
_quests = {"Не лает, не кусает, а в дом не пускает": ["Замок", "Охранник", "Сторож"],
           "Нет ушей, а слышит, нету рук, а пишет": ["Магнитофон", "Магнитола"]
           }

_results = dict()


def _save_result(quest: str, answer_count: int):
    _results.setdefault(quest, answer_count)


def _run_quest(quest: str, answers: list[str], count) -> int:
    for i in range(len(answers)):
        answers[i] = answers[i].lower()
    print("Загадка: ", quest)
    for i in range(count):
        res = input("  введите ответ: ")
        if res.lower() in answers:
            return i + 1
        print("  ответ неверный")
    return 0


def do_quests():
    for k, v in _quests.items():
        n = _run_quest(k, v, _MAX_ATTEMPTS)
        _save_result(k, n)
        if n > 0:
            print(f"Угадали с {n} попытки!")
        else:
            print(f"Не угадали, правильные ответы: {v}")
        print()


def show_results():
    """ Возвращает результат викторины, какой вопрос и с какой попытки отгадан, или не отгадан """
    for k, v in {k: "не отгадано" if v == 0 else f"отгадано за {v} попытку" for k, v in _results.items()}.items():
        print(f"Загадка: '{k}', результат: '{v}")


if __name__ == '__main__':
    do_quests()
    show_results()
