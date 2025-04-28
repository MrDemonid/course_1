# PYTEST

# import pytest  # нужен только для запуска тестов из файла.


def sum_num(a, b):
    return a + b


# функция тестирования
def test_sum():
    assert sum_num(2, 2) == 4, "Здесь это не работает"

def test_sum2():
    assert sum_num(3, 3) == 6

if __name__ == '__main__':
    test_sum2()
    test_sum()
