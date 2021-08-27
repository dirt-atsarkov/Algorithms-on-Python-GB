# Проанализировать скорость и сложность одного любого алгоритма,
# разработанных в рамках домашнего задания первых трех уроков.
# Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.


# В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве.

import random
import timeit

list_1 = [random.randint(-100, 100) for _ in range(15)]
print(list_1)

def my_func_1(num_list):
    max_neg = min(num_list)
    max_id = 0
    for i in num_list:
        if 0 > i > max_neg:
            max_neg = i
            max_id = list_1.index(i)

def my_func_2(num_list):
    new_list = [i for i in num_list if i < 0]
    maximum = max(new_list)
    idx = new_list.index(maximum)

print(timeit.timeit("my_func_1(list_1)"))
print(timeit.timeit("my_func_2(list_1)"))
