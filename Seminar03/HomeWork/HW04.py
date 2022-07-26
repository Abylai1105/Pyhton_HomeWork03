# 4 - Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# *Пример:*

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

number = int(input('Введите десятичное число: '))
bin = ' '
while number > 2:
    bin = str(number % 2) + bin
    number //= 2
bin = str(number // 2) + str(number % 2) + bin
print(bin)