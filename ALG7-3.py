# Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
#  Найти в массиве медиану. Медианой называется элемент ряда, делящий его на две
#  равные части: в одной находятся элементы, которые не меньше медианы, в другой – не больше ее.

import random


def median(array, k):
    if len(array) == 1:
        return array[0]

    pivot = random.choice(array)

    left_el = [el for el in array if el < pivot]
    right_el = [el for el in array if el > pivot]
    pivots = [el for el in array if el == pivot]

    if k < len(left_el):
        return median(left_el, k)
    elif k < len(left_el) + len(pivots):
        return pivots[0]
    else:
        return median(right_el, k - len(left_el) - len(pivots))


m = 5
list = [random.randint(0, 100) for _ in range(2 * m + 1)]
print(list)
print(median(list, len(list) / 2))
