#2. Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.

from operator import index
from unittest import result


lst = ['21', '1', '21', 'er']
find_number = 21
count = 2
def find_number_in_list(lst_to_seek:list,number:int,count:int):
    for i in range(0,len(lst_to_seek)):
        if lst_to_seek[i] == str(number):
            count = count - 1
        if count == 0:
            return i
    return -1
    j = 0

pos_number = find_number_in_list(lst,find_number,count)
if pos_number != -1:
    print(pos_number)
else:
    print('В списке нет такого числа')
