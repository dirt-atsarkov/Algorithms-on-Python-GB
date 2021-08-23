# 4. Определить, какое число в массиве встречается чаще всего.

import random

list_1=[random.randint(0, 100) for i in range(35)]

dict_num = dict.fromkeys(list_1, 0)
for num in list_1:
    dict_num[num] += 1

max_num = 0
for key in dict_num:
    if dict_num[key] > max_num:
        max_key = key
        max_num = dict_num[key]

print(f'{list_1} \nsamoe chastoe chislo: {max_key} ({max_num} vhozhdeniy)')