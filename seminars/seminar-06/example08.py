"""
Задание №8
� Создайте пакет с всеми модулями, которые вы создали за время занятия.
� Добавьте в __init__ пакета имена модулей внутри дандер __all__.
� В модулях создайте дандер __all__ и укажите только те функции, которые могут верно работать за пределами модуля.
"""
from semmodules.check_date import *
from semmodules.guessing_mystery import *
import semmodules.guessing_number as gn

print(is_valid_date('12.12.2025'))

do_quests()
show_results()

gn.bulls_and_cows()

