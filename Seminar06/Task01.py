# Написать программу вычисления арифметического выражения заданного строкой. 
# Используются операции +,-,/,*. приоритет операций стандартный. 
# Пример: 2+2 => 4; 1+2*3 => 7; 1-2*3 => -5
# 10/2 * 5
# Допольнительно: добавить возможность использование скобок,
# меняющий приоритет операций : (1+2)*3 => 9
# ((1+3) * (4 - 5)) * 4

input_res = '1-2+3+9-2'
lis_num = []
lis_operation = []
for i in range(len(input_res)):
    if input_res[i].isdigit():
        lis_num.append(int(input_res[i]))
    elif input_res[i].find('%'):
        lis_operation.append(input_res[i])

res = 0
for i in range(len(lis_operation)):
    if lis_operation[i] == '+':
        res = lis_num[i] + lis_num[i+1]
        lis_num[i+1] = res
    elif lis_operation[i] == '-':
        res = lis_num[i] - lis_num[i-1]
        lis_num[i+1] = res
    

       
print(lis_num)
print(lis_operation)
print(res)







# for i,char in enumerate(input_res):
#     if char in '+-*/':