# 1. Задайте список. Напишите программу, которая определит, 
# присутствует ли в заданном списке строк некое число.

# import numbers
# from os import POSIX_FADV_WILLNEED
# from random import random
# from unittest import result


lst = ['3', '2f3', 'rw1', '221']
find_number = 3
def find_number_in_list(lst_to_seek:list,number:int):
    lst_index = {}
    j = 0
    for char in lst_to_seek:
        for symbol in char:
            lst_index[j] = lst_to_seek.index(char)
            j = j + 1
    return list(lst_index.values())

pos_number = find_number_in_list(lst,find_number)
if len(pos_number) != 0:
    print(pos_number)
else:
    print('В списке нет такого числа')


