#
# Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке.
#

DIST_FROM_TABLES = "        "

def draw_rows(rows):
    for j in range(2, 11):
        for i in rows:
            print(f"{i} X {str(j).rjust(2)} = {str((i * j)).rjust(2)}", end=DIST_FROM_TABLES)
        print()
    print()


draw_rows([2, 3, 4, 5])
draw_rows([6, 7, 8, 9])
