import csv


# Предметы для CSV
subjects = ["Математика", "Физика", "История", "Литература"]


with open("../subjects.csv", mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(subjects)
