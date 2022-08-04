# 2- Найти сумму чисел списка стоящих на нечетной позиции


numbers = [9, 4, 23, 54, 7, 49, 75, 323, 65]


def get_sum(num):
    return sum(num[1::2])
                                    

print(get_sum(numbers))