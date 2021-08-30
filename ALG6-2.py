# Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
# Проанализировать результат и определить программы с наиболее эффективным использованием памяти.

import sys

dict = dict.fromkeys(range(2, 10), 0)
for num in range(2, 100):
    for i in range(2, 10):
        if num % i == 0:
            dict[i] += 1

for key in dict:
    print(f"{key} kratny {dict[key]} chisel")

sum_size = 0
sum_size += sys.getsizeof(dict)
sum_size += sys.getsizeof(num)
sum_size += sys.getsizeof(i)
sum_size += sys.getsizeof(key)


