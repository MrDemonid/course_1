"""
Задача 5. Конвертация CSV в JSON с изменением структуры данных.

Напишите скрипт, который считывает данные из CSV файла и сохраняет их в
JSON файл с другой структурой.
CSV файл содержит данные о книгах (название, автор, год издания).
В JSON файле данные должны быть сгруппированы по авторам,
а книги каждого автора должны быть записаны как список.

Пример: Из файла books.csv нужно создать файл books_by_author.json, где книги сгруппированы по авторам.
"""
import csv
import json
import os.path


def sort_to_authors(src, dst):
    if os.path.exists(src) and os.path.isfile(src):
        with open(src, 'r', newline='', encoding='utf-8') as f:
            rd = csv.DictReader(f)
            res = dict()
            for line in rd:
                author = line['Author']
                book = {'Title': line['Title'], 'Date': line['Date']}
                if not author in res:
                    res[author] = list()
                res[author].append(book)

        with open(dst, 'w', encoding='utf-8') as f:
            json.dump(res, f, ensure_ascii=False, indent=4)

    else:
        print(f"Error: file {src} not found!")


if __name__ == '__main__':
    sort_to_authors('./datas/zad_5/books.csv', './datas/zad_5/books.json')
