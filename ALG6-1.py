# Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
# Проанализировать результат и определить программы с наиболее эффективным использованием памяти.

import sys
import random

list_1=[random.randint(0, 100) for i in range(18)]
print(list_1)
min_id = list_1.index(min(list_1))
max_id = list_1.index(max(list_1))
sum = 0

for i in list_1:
    if max_id > list_1.index(i) > min_id or max_id < list_1.index(i) < min_id:
        sum += i

print(f"SUMM : {sum}")

sum_size = 0
sum_size += sys.getsizeof(list_1)
sum_size += sys.getsizeof(min_id)
sum_size += sys.getsizeof(max_id)
sum_size += sys.getsizeof(i)
sum_size += sys.getsizeof(sum)

print('Variables size : ', sum_size)