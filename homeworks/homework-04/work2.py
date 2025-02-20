"""
Задача 2. Недоделка
Вы пришли на работу в компанию по разработке игр, целевая аудитория —
дети и их родители. У предыдущего программиста было задание сделать две
игры в одном приложении, чтобы пользователь мог выбирать одну из них.
Однако программист, на место которого вы пришли, перед увольнением не
успел выполнить эту задачу и оставил только небольшой шаблон проекта.
Используя этот шаблон, реализуйте игры «Камень, ножницы, бумага» и «Угадай
число».
Правила игры «Камень, ножницы, бумага»: программа запрашивает у
пользователя строку и выводит, победил он или проиграл. Камень бьёт
ножницы, ножницы режут бумагу, бумага кроет камень.
Правила игры «Угадай число»: программа запрашивает у пользователя число
до тех пор, пока он не отгадает загаданное.

def rock_paper_scissors():
# Здесь будет игра «Камень, ножницы, бумага»
def guess_the_number():
# Здесь будет игра «Угадай число»
def mainMenu():
# Здесь главное меню игры
mainMenu():
pass
"""
from random import random, randint


# игра «Камень, ножницы, бумага»
def rock_paper_scissors():
    names = ['rock', 'scissors', 'paper']
    computer = randint(1, 3)
    player = int(input("Enter:\n    1 - rock\n    2 - scissors\n    3 - paper\n> "))
    if player < 1 or player > 3:
        print("Never number!")
        return
    print(f"computer select is {names[computer-1]}")
    if player == 1 and computer == 2 or player == 2 and computer == 3 or player == 3 and computer == 1:
        print("Player win!")
    elif player == computer:
        print("Draw!")
    else:
        print("Player lose!")


# игра «Угадай число»
def guess_the_number():
    computer = randint(1, 100)
    moves = 1
    while True:
        player = int(input("Enter the number: "))
        if player == computer:
            print(f"Congratulations! You won in {moves} moves.")
            break
        if player > computer:
            print("The number is greater than necessary")
        else:
            print("The number is less than required")
        moves += 1


def mainMenu():
    while True:
        menu = int(input("\nEnter play:\n    1 - 'Rock/Scissors/Paper\n    2 - 'Guess the number'\n    other - exit\n> "))
        if menu == 1:
            rock_paper_scissors()
        elif menu == 2:
            guess_the_number()
        else:
            quit()

mainMenu()
