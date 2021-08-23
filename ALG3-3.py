# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

list_1=[random.randint(0, 100) for i in range(15)]

max = list_1[0]
min = list_1[0]
max_id = 0
min_id = 0


print(list_1)
for i in list_1:
    if i > max:
        max = i
        max_id = list_1.index(i)
    if i < min:
        min = i
        min_id = list_1.index(i)

list_1[max_id], list_1[min_id] = list_1[min_id], list_1[max_id]

print(list_1)
