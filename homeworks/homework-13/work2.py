"""
Задача 2. Чат.

Реализуйте программу - чат, в котором могут участвовать сразу несколько человек, то
есть программа может работать одновременно для нескольких пользователей.
При запуске запрашивается имя пользователя.
После этого он выбирает одно из действий:
    1. Посмотреть текущий текст чата
    2. Отправить сообщение (затем вводит сообщение) Действия запрашиваются бесконечно.
"""


class Chat:
    def __init__(self, fn="./datas/work2_chat.txt"):
        self.fn = fn

    def show_history(self):
        """ Выводит пользователю историю сообщений. """
        try:
            with open(self.fn, 'rt', encoding='utf-8') as f:
                lines = f.readlines()
                print("".join(lines))
        except FileNotFoundError:
            print("История пуста!")

    def add_message(self, name, msg):
        if not name is None and not msg is None:
            with open(self.fn, 'at', encoding='utf-8') as f:
                f.write(f"{name}: {msg}\n")

    def do_run(self):
        """ Основной цикл чата для текущего пользователя. """
        name = input("Введите свое имя: ")
        print("Введите: 1 - для показа истории чата, 2 - для сообщения, 3 - для выхода.")
        if not name is None:
            while 1:
                cmd = input()
                if cmd == '1':
                    self.show_history()
                elif cmd == '2':
                    msg = input("Введите сообщение: ")
                    self.add_message(name, msg)
                elif cmd == '3':
                    break


if __name__ == '__main__':
    chat = Chat()
    chat.do_run()
