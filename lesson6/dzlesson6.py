# 1. LIST COMPREHANSION

# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу
# между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 10.01] => 0.19

#  СТАРОЕ РЕШЕНИЕ

list = [1.1, 1.2, 3.1, 10.01]
list2 = []
for i in range(len(list)):
    list2.append(round((list[i] - (list[i]//1)), 2))
print(list2)
print(max(list2) - min(list2))

# НОВОЕ РЕШЕНИЕ

list = [1.1, 1.2, 3.1, 10.01]
list2 = [(round((list[i] - (list[i]//1)), 2)) for i in range(len(list))]
print(list2)
print(max(list2) - min(list2))

# 2. ФУНКЦИЯ MAP

# Напишите программу, которая будет преобразовывать десятичное число в двоичное (без встроенных функций).

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

#  СТАРОЕ РЕШЕНИЕ

number = 45
list = []
while number != 0:
    list.append(number % 2)
    number = number // 2
list.reverse()
for i in range(len(list)):
    list[i] = str(list[i])
result = ''.join(list)
print(result)

# НОВОЕ РЕШЕНИЕ

number = 45
list = []
while number != 0:
    list.append(number % 2)
    number = number // 2
list.reverse()
list = map(str, list)
result = ''.join(list)
print(result)

# 3. ФУНКЦИЯ FILTER

# СТАРОЕ РЕШЕНИЕ 

# Задайте последовательность чисел. Напишите программу, которая выведет список 
# неповторяющихся элементов исходной последовательности.
# [1, 1, 2, 3, 4, 5, 5] -> [2, 3, 4]

lst = [1, 1, 2, 3, 4, 5, 5]
list2 = [i for i in lst if lst.count(i) == 1]
print(list2)

# НОВОЕ РЕШЕНИЕ

lst = [1, 1, 2, 3, 4, 5, 5]
list2 = list(filter((lambda x: lst.count(x) == 1), lst))
print(list2)