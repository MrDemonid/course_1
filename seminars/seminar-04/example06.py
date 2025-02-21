"""
Задание №6
✔ Функция получает на вход список чисел и два индекса.
✔ Вернуть сумму чисел между переданными индексами.
✔ Если индекс выходит за пределы списка, сумма считается до конца и/или начала списка.
"""

l = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def sum_between_indexes(lst: list, start, end):
    if start > end:
        start, end = end, start
    start = max(start + 1, 0)
    end = min(end - 1, len(lst)-1)
    if start > end:
        return None
    print(start, end)
    print((lst[start:end+1]))
    return sum((lst[start:end+1]))

print(sum(l))
print(sum_between_indexes(l, 0, 8))

