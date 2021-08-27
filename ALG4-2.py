# Написать два алгоритма нахождения i-го по счёту простого числа.
# Без использования «Решета Эратосфена»;
# Используя алгоритм «Решето Эратосфена»
# Примечание ко всему домашнему заданию: Проанализировать скорость и сложность алгоритмов.
# Результаты анализа сохранить в виде комментариев в файле с кодом.

import cProfile


numb = int(input('vvesti chislo dlya procheta : '))
lst = [i for i in range(numb * numb)]


# Вариант 1. Решето Эратосфена.


def sieve(num_list, idx):
    num_list[1] = 0
    i = 2
    s_num_list = []
    while len(s_num_list) < idx:
        if num_list[i] != 0:
            s_num_list.append(num_list[i])
            j = i * 2
            while j < len(num_list):
                num_list[j] = 0
                j += i
        i += 1
    return s_num_list[-1]

cProfile.run("sieve(lst, numb)")

# numb = 120
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.010    0.010 <string>:1(<module>)
#        1    0.007    0.007    0.010    0.010 ALG4-2.py:17(sieve)
#        1    0.000    0.000    0.010    0.010 {built-in method builtins.exec}
#    31411    0.003    0.000    0.003    0.000 {built-in method builtins.len}
#      120    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}



# Вариант 2. Перебор.

def simple_num(num_list, idx):
    num_list[1] = 0
    s_nums = []
    for i in range(2, len(num_list)):
        for num in s_nums:
            if num_list[i] % num == 0:
                break
        else:
            s_nums.append(num_list[i])
        if len(s_nums) == idx:
            return s_nums[-1]

cProfile.run("simple_num(lst, numb)")


# numb = 120
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#        1    0.001    0.001    0.001    0.001 ALG4-2.py:44(simple_num)
#        1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#      659    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#      120    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


# Сложность 1го алгоритма (Эратосфен) = O(n**2)
# Сложность 2го алгоритма (Перебор)  = O(n**2)
# Сложность алгоритмов объясняется вложенностью циклов.
# Несмотря на то, что сложность у обоих алгоритмов = O(n**2), очень заметна разница в скорости.
