# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

import random

list_1=[random.randint(0, 100) for i in range(15)]
print(list_1)
min_id = list_1.index(min(list_1))
max_id = list_1.index(max(list_1))
sum = 0

for i in list_1:
    if max_id > list_1.index(i) > min_id or max_id < list_1.index(i) < min_id:
        sum += i

print(f"SUMM : {sum}")