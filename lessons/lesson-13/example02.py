def hundred_div_num(div: float, text: str = None) -> tuple[int, float]:
    while True:
        try:
            num = int(input(text))
            res = div / num
            break
        except ValueError as e:
            print(f'Ваш ввод привёл к ошибке ValueError: {e}\n'f'Попробуйте снова')
        except ZeroDivisionError as e:
            res = float('inf')
            break
    return num, res


if __name__ == '__main__':
    n, d = hundred_div_num(100, 'Введите целый делитель: ')
    print(f'Результат операции: "100 / {n} = {d}"')
