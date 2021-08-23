# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.

import random

list_1=[random.randint(-100, 100) for i in range(15)]
print(list_1)
max_neg = min(list_1)
max_id = 0
for i in list_1:
    if 0 > i > max_neg:
        max_neg = i
        max_id = list_1.index(i)

print(f"ID : {max_id} NUMBER : {max_neg}")
