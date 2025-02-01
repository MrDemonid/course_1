#
# Напишите программу, которая запрашивает год и проверяет его на високосность.
# Обязательно учтите год ввода Григорианского календаря
# В коде должны быть один input и один print
#

def is_visokos(year):
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        return "високосный"
    return "не високосный"


'''
    тернарный аналог
'''
def is_visokos2(year):
    return "високосный" if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0) else "не високосный"


year = int(input("Введите год: "))
print(f"Год {year} {is_visokos(year)}")
print(f"Год {year} {is_visokos2(year)}")
