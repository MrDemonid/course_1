"""
Задача 3. Проверка палиндрома.
    Напишите программу, которая принимает строку и определяет, является ли она
палиндромом (читается одинаково с обеих сторон).
"""

inp = "Море могуче. В тон ему, шумен отвечу Гомером".lower()
src = "".join([i for i in inp if i.isalpha()])

# Вариант 1. Самый быстрый

for i in range(len(src) // 2):
    if src[i] != src[len(src) - i - 1]:
        print(">Строка не является палиндромом")
        quit()
print(">Строка палиндром")

# Вариант 2, замороченный

odd_char = set()

for ch in src:
    print(ch, end=", ")
    if ch in odd_char:
        odd_char.remove(ch)
    else:
        odd_char.add(ch)

print(len(odd_char))
if len(odd_char) <= 1:
    print("Строка палиндром")
else:
    print("Строка не является палиндромом")
