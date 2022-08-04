# 3- Найти расстояние между двумя точками пространства(числа вводятся через пробел)

from functools import reduce
first_point = list(
    map(int, input('Введите координаты первой точки: ').split()))
second_point = list(
    map(int, input('Введите координаты второй точки: ').split()))
distance = reduce(lambda a, b: (a + b)**(1/2),
                  (map(lambda p: (p[1] - p[0])**2, zip(first_point, second_point))))
print(distance)