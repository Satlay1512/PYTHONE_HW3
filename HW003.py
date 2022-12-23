# Урок 3. Данные, функции и модули в Python
# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

## list = list(map(float,input("Введите целые числа через пробел ->").split()))
# list =[2, 3, 5, 9, 3]
# result = 0
# for i in range(1, len(list), 2):
#     result += list[i]
#     print(list[i])
# print(f" сумма нечетных элементов списка {list} равно -> {result}")


# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

## list = list(map(float,input("Введите целые числа через пробел ->").split()))
# list = [2, 3, 4, 5, 6]
# # list = [2, 3, 5, 6]
# list_num = []
# for i in range((len(list) // 2 + len(list) % 2)):
#     new_num = list[i+1] * list[-i-1]
#     list_num.append(new_num)
# print(f'Список: {list} -> произведение пар чисел: {list_num}')


# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между
# максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5,02 10.01] => 0.19
## list = list(map(float,input("Введите дробные числа через пробел ->").split()))
# list = [1.1, 1.2, 3.1, 5.01, 10.09]
# list_num = []
# for i in range(len(list)):
#     new_num = round((list[i]%1), 3)
#     list_num.append(new_num)
# result = round(max(list_num) - min(list_num), 4)
# print(list_num)
# print(f" {result}")

# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

# number = int(input("Введите целое число ->"))
 
# binary_number = " "
 
# while number > 0:
#     binary_number = str(number % 2) + binary_number
#     number = number // 2
 
# print(f"{binary_number}")


# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
# [Негафибоначчи]

# n = int(input('Введите число: '))
# fib_list1=[0, 1]
# fib_list2 = [1]
# fib1 = 0
# fib2 = 1
# fib_1 = 0
# fib_2 = 1
# for _ in range(n-1):
#     fib1, fib2 = fib2, fib1 + fib2
#     fib_list1.append(fib2)
#     fib_1, fib_2 = fib_2, fib_1 - fib_2
#     fib_list2.append(fib_2)
# fib_list2.reverse()
# fib_list = fib_list2.copy()
# fib_list.extend(fib_list1)
# print(f'Для числа {n} последовательность Фибоначчи и Негафибоначчи: {fib_list}')