# 2. Создать и заполнить файл случайными целыми значениями. 
# Выполнить сортировку содержимого файла по возрастанию. (не использовать sort и sorted)

from itertools import product
from array import array
from random import randint
from tkinter import SW


def get_random_list() -> list:
    lst = [randint(10,99) for x in range(6)]
    return lst

my_list = get_random_list()
print(my_list)

def sort_list(array: list) -> list:
    swap = True
    while swap:
        swap = False
        for i in range(len(array) - 1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                swap = True
    return array

sorted_list = sort_list(my_list)

def main():
    print(sorted_list)
