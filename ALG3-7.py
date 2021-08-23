# 7. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.

import random

list_1=[random.randint(0, 100) for i in range(15)]
print(list_1)
min_1 = min(list_1)
list_1.remove(min_1)
min_2 = min(list_1)
print(f"MIN1 = {min_1}, MIN2 = {min_2}")

