import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime


df = pd.read_excel("C:/Users/Andrey/Desktop/АД.xlsx", engine="openpyxl")


month_map = {
    'янв': '01', 'фев': '02', 'мар': '03', 'апр': '04',
    'май': '05', 'июн': '06', 'июл': '07', 'авг': '08',
    'сен': '09', 'окт': '10', 'ноя': '11', 'дек': '12'
}

# Нормализация даты, то есть замена названия месяца на его номер.
def normalize_date(date_str):
    for rus, num in month_map.items():
        if rus in date_str:
            return date_str.replace(rus, num)
    return date_str


# Приведение даты и времени к строковому типу (на случай, если Excel форматирует по-своему)
df["Дата"] = df["Дата"].astype(str).apply(normalize_date)
df["Время"] = df["Время"].fillna("12:00").astype(str).str.strip()

# Объединение в datetime
df["datetime"] = pd.to_datetime(df["Дата"] + " " + df["Время"], errors="coerce")


# Преобразование давления и пульса в числовой тип
df["Верхнее"] = pd.to_numeric(df["Верхнее"], errors="coerce")
df["Нижнее"] = pd.to_numeric(df["Нижнее"], errors="coerce")
df["Пульс"] = pd.to_numeric(df["Пульс"], errors="coerce")

# Удаляем строки без валидной даты
df.dropna(subset=["datetime"], inplace=True)

# Сортировка по дате
df = df.sort_values("datetime")

# Получаем диапазон дат
start_date = df["datetime"].min()
end_date = df["datetime"].max()

#
plt.figure(figsize=(14, 8))

# --- График давления ---
plt.subplot(2, 1, 1)
plt.plot(df["datetime"], df["Верхнее"], label="Систолическое (Верхнее)", color="red", marker='o')
plt.plot(df["datetime"], df["Нижнее"], label="Диастолическое (Нижнее)", color="blue", marker='o')
plt.axvline(datetime(2025, 5, 17, 6, 17), color='green', linestyle='--', label='Начало Престариума')

plt.title("Артериальное давление")
plt.ylabel("Давление (мм рт. ст.)")
plt.xlim([start_date, end_date])
plt.grid(True)
plt.legend(loc="lower center")
plt.xticks(rotation=45)

# --- График пульса ---
plt.subplot(2, 1, 2)
plt.plot(df["datetime"], df["Пульс"], label="Пульс", color="purple", marker='o')
plt.axvline(datetime(2025, 5, 17, 6, 17), color='green', linestyle='--', label='Начало Престариума')

plt.title("Пульс")
plt.ylabel("Удары в минуту")
plt.xlabel("Дата и время")
plt.xlim([start_date, end_date])
plt.grid(True)
plt.legend(loc="best")
plt.xticks(rotation=45)         # поворот подписей оси X для читаемости

plt.tight_layout()
plt.show()
