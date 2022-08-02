#Задана натуральная степень n. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени n.
# *Пример:
#
#
# n=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
#n =4 => x**4 + 8*x**3 + 2*x² + 4*x + 5 = 0
#Все коэффициенты кроме нулевого могут быть нулем - такого элемента в полиноме не будет
#если коэффициент равен 1, то 1 указывается только при свободном элементе.При x² + 5 = 0 - это 5.

from cgitb import reset
import numbers
import random
from unittest import result

import Penschii_A_Function as PF

number_N = PF.input_number_examination(text_in_input = "n : ", case_def = 1)

test_bool = True
while test_bool:
    list_1 = [random.randint(0, 100) for i in range(number_N+1)]
    if list_1[0] != 0:
        test_bool = False


list_2 = ['x' for i in range(number_N+1)]

result = ""
for i in range(0, len(list_1)):
    if list_1[i] == 1 and number_N > 1:
        result += f"{list_2[i]}^" + f"{number_N}"
    elif list_1[i] != 0 and number_N > 1:
        result += f"{list_1[i]}*" + f"{list_2[i]}^" + f"{number_N}"
    elif list_1[i] == 1 and number_N == 1:
        result += f"{list_2[i]}"
    elif list_1[i] == 1 and number_N == 0:
        result += f"{list_1[i]}"
    elif list_1[i] != 0 and number_N == 1:
        result += f"{list_1[i]}*" + f"{list_2[i]}"
    elif list_1[i] != 0 and number_N == 0:
        result += f"{list_1[i]}"

if i < len(list_1) - 1:
    result[-3:len(result)]

result += " =0"

print(result)


number_N = PF.input_number_examination(text_in_input = "n : ", case_def = 1)

test_bool = True
while test_bool:
    coef_1 = [random.randint(0, 100) for i in range(number_N+1)]
    if coef_1[0] != 0:
        test_bool = False


coef_2 = ['x' if i < number_N else '' for i in range(0, number_N+1)]
coef_3 = [i if i > 1 else '' for i in range(number_N - 1, -1)]

list_new = list(zip(coef_1, coef_2, coef_3))

print(list_new)

list_final = []