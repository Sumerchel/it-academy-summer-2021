"""Выведите n-ое число Фибоначчи, используя только временные переменные,
циклические операторы и условные операторы. n - вводится"""


n = int(input("Введите какое число фибоначи нужно вывести(отсчёт идёт с 1): "))
num1, num2 = (0, 1)  # Задаём 1 и 2 число фибоначи
i = 1
while i < n:
    num1, num2 = (num2, num1 + num2)  # Алгоритм фибоначи
    i += 1
    if i == n:  # Проверяем является ли заданное число равным нашему
        print(num1)


