# Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.

# *Пример:*
# - Для N = 5: 1, -3, 9, -27, 81

from unittest import result


n = int(input('Введите число N: '))
result = 1
for i in range(n):
    print(result, end=' ')
    result *= -3