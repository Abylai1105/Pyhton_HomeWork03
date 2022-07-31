# 1. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.


from itertools import product
from random import randint


def product_elements() -> int:
    with open('indexes.txt', 'r', encoding = 'utf-8') as file:
        indexes = file.read().split('\n')
    n = int(input('Введите длину списка: '))
    my_list = []
    for i in range(n):
        my_list.append(randint(-n, n))
    print('Исходный список: ', my_list)
    print('Исходный множетель: ' , ' , '.join(indexes))
    product = 1
    for i in range(len(my_list)):
        if str(i) in indexes:
            product *= my_list[i]
    return product

def main():
    print(product_elements())

if __name__ == '__main__':
    main()

















# with open('text', mode = 'r') as file:
    #print(file(read))

# my_lst = [3, -5, 21, 7, -9]

# data = open('file.txt', 'w')
# for i in my_lst:
#     data.write(str(my_lst.index(i)))
# data.close()

# def create_lst(number: int):
#     import random
#     lst = []
#     for i in range(0, number):
#         lst.append(random.randint(0, 100))
#     return lst
# print(create_lst(5))

# def writelist(my_lst: list):
#     data = open('file.txt', 'w')
#     for i in my_lst:
#         data.write(str(my_lst.index(i)))
#     data.close()
# writelist(create_lst(10))
