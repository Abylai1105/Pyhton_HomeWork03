# 5 - Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# *Пример:*

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

n = int(input('Введите число: '))
fibonachi = [0,1]
for i in range(2, n + 1):
    fibonachi.append(fibonachi[i - 1] + fibonachi[i - 2])

minus = []
for i in range(1, len(fibonachi)):
    minus = [pow(1, i + 1) * -fibonachi[i]] + minus

print(minus + fibonachi)