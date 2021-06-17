"""В этом небольшом задании вам дается строка чисел, разделенных пробелами, и вы должны вернуть самое
высокое и самое низкое число.
Пример:
high_and_low("1 2 3 4 5")  # return "5 1"
high_and_low("1 2 -3 4 5") # return "5 -3"
high_and_low("1 9 3 4 -5") # return "9 -5"
Примечания:
Все номера действительны Int32- нет необходимость чтобы подтвердить их.
Во входной строке всегда будет присутствовать хотя бы одно число.
Выходная строка должна состоять из двух чисел, разделенных одним пробелом,
причем наибольшее число должно быть первым."""


high_low = list(map(int, input("Введите список чисел через пробел: ").split()))
print("Максимальное число:", max(high_low), "Минимальное число:", min(high_low))
