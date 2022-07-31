# list = []

# for i in range(1, 101):
#     #if(i%2 == 0):
#         list.append(i)

# print(list)

# list = [i for i in range(1, 21) if i%2 == 0]
# print(list)

# list = [(i, i) for i in range(1, 21) if i%2 == 0]
# print(list)

# from posixpath import split
# from unittest import res


# def f(x):
#     return x ** 3

# list = [(i, f(i)) for i in range(1, 21) if i%2 == 0]
# print(list)



# list1 = [1, 2, 3, 5, 8, 15, 23, 38]
# def f(x):
#     return x**2

# list = [(i, f(i)) for i in list1 if i%2 == 0]
# print(list)




# def select(f, col):
#     return [f(x) for x in col]


# def where(f, col):
#     return [x for x in col if f(x)]

# data = '1, 2, 3, 5, 8, 15, 23, 38'.split()

# res = select(int, data)
# res = where(lambda x: not x % 2, res)
# res = select(lambda x: (x, x**2), res)
# print(res)



# li = [x for x in range(1, 20)]

# li = list(map(lambda x:x+10, li))
# print(li)


# Функция map

# data = list(map(int,input().split()))
# print(data)


# data = list(map(int,'1 2 3'.split()))

# for e in data:
#     print(e)

# print('--')

# for e in data:
#     print(e)




# def where(f, col):
#     return [x for x in col if f(x)]

# data = '1, 2, 3, 5, 8, 15, 23, 38'.split()

# res = map(int, data)
# res = filter(lambda x: not x % 2, res)
# res = list(map(lambda x: (x, x**2), res))
# print(res)



## Функция Filter
# Функция filter() применяет указанную функцию к
# каждому элементу итерируемого объекта и
# возвращает итератор с теми объектами, для
# которых функция вернула True.
# f(x) ⇒ x - чётное
# filter(f, [ 1, 2, 3, 4,5])
#  ↓
#  [ 2, 4 ]
# Нельзя пройтись дважды

# data = [x for x in range(10)]

# res = list(filter(lambda x: not x%2, data))
# print(res)




## Функция zip
# Функция zip() применяется к набору итерируемых
# объектов и возвращает итератор с кортежами из
# элементов входных данных.
# Количество элементов в результате равно минимальному количеству элементов входного набора
# zip ([1, 2, 3], [ ‘о‘, ‘д‘, ‘т‘], [‘f’,’s’,’t’])
#  ↓
# [(1, 'о', 'f'), (2, 'д', 's'), (3, 'т', 't')]
# Нельзя пройтись дважды

# users = ['user1', 'user2', 'user3', 'user4', 'user5']
# ids = [1, 2, 3, 4, 5]
# salary = [111, 222, 333]
# data = list(zip(users, ids, salary))
# print(data)


##Функция enumerate
# Функция enumerate() применяется к итерируемому
# объекту и возвращает новый итератор с кортежами
# из индекса и элементов входных данных.
# enumerate(['Казань', 'Смоленск', 'Рыбки', 'Чикаго'])
#  ↓
# [(0, 'Казань'), (1, 'Смоленск'), (2, 'Рыбки'), (3, 'Чикаго')]
# Нельзя пройтись дважды

users = ['user1', 'user2', 'user3', 'user4', 'user5']
ids = [1, 4, 21, 6, 9]
salary = [111, 222, 333]
data = list(enumerate(users))
print(data)