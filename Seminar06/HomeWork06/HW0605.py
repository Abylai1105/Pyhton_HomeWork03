# 5- Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, \
#     второй и предпоследний и т.д.
import math

numbers = [6, 2, 7, 1, 4, 6, 5, 7, 8, 4, 2, 8, 8, 9, 1]


def mult_list(nums):
    return [nums[i] * nums[-i-1] for i in range(math.ceil(len(nums)/2))]

print(mult_list(numbers))