# Перед вами несколько строк doctest. Напишите что должна делать программа,
# чтобы пройти тесты. У вас 3 минуты.


def say(s, count=2, delimiter=' '):
    """
    >>> say('Hello')
    Hello Hello
    >>> say('Hi', 5)
    Hi Hi Hi Hi Hi
    >>> say('cat', 3, '(=^.^=)')
    cat(=^.^=)cat(=^.^=)cat
    """
    res = delimiter.join([f"{s}"] * count)
    print(res)


if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True)
