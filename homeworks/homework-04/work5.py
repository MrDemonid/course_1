"""
Задача 5. Яйца
В рамках программы колонизации Марса компания «Спейс Инжиниринг»
вывела особую породу черепах, которые, по задумке, должны размножаться,
откладывая яйца в марсианском грунте. Откладывать яйца слишком близко к
поверхности опасно из-за радиации, а слишком глубоко — из-за давления
грунта и недостатка кислорода. Вообще, факторов очень много, но
специалисты проделали большую работу и предположили, что уровень
опасности для черепашьих яиц рассчитывается по формуле: D = x^3 − 3x^2 −
12x + 10, где x — глубина кладки в метрах, а D — уровень опасности в
условных единицах. Для тестирования гипотезы нужно взять пробу грунта на
безопасной, согласно формуле, глубине.
Напишите программу, находящую такое значение глубины х, при котором
уровень опасности как можно более близок к нулю. На вход программе
подаётся максимально допустимое отклонение уровня опасности от нуля, а
программа должна рассчитать приблизительное значение х, удовлетворяющее
этому отклонению. Известно, что глубина точно больше нуля и меньше четырёх
метров. Обеспечьте контроль ввода.
Пример:
Введите максимально допустимый уровень опасности: 0.01
Приблизительная глубина безопасной кладки: 0.732421875 м
"""

MIN_DEPTH = 0.0
MAX_DEPTH = 4.0

'''
    Calculation of the danger level.
'''
calc_danger = lambda x: x ** 3 - 3 * x ** 2 - 12 * x + 10


'''
    Finding the depth with the least level of danger.
'''
def calculate_depth(max_danger):
    min_depth = MIN_DEPTH
    max_depth = MAX_DEPTH
    middle_depth = (min_depth + max_depth) / 2
    middle_danger = calc_danger(middle_depth)           # danger level at medium depth

    while abs(middle_danger) > max_danger:
        # narrowing the boundaries of acceptable depths
        if middle_danger > 0:
            min_depth = middle_depth
        else:
            max_depth = middle_depth
        middle_depth = (min_depth + max_depth) / 2
        middle_danger = calc_danger(middle_depth)
    return middle_depth


def main():
    max_danger = float(input('Enter the acceptable level of danger:'))
    if max_danger >= 0:
        depth = calculate_depth(max_danger)
        print(f'Safe masonry depth: {depth} м')
    else:
        print('Invalid value!')


main()
