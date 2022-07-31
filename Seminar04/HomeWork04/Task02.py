# 2- Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности. 
# Посмотрели, что такое множество? Вот здесь его не используйте.

subsequence  = [4, 5, 6, 4, 5, 6, 4, 5, 6]


def sort_subsequence(sub: list):
    sub2 = sorted(sub)
    n = []
    for i in sub2:
        if i not in n:
            n.append(i)
    return n

print(sort_subsequence(subsequence))