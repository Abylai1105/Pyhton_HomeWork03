# 2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
# Примеры:

# - 1, 4, 8, 7, 5 -> 8
# - 78, 55, 36, 90, 2 -> 90

list_numbers = [3, 9, 8 , 4, 6]
max_numbers = list_numbers[0]
for item in list_numbers:
    if max_numbers < item:
        max_numbers = item
print(max_numbers)