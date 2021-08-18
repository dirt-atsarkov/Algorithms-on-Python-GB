# Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.

num = int(input('vvedote tseloe chislo. dlya vihoda vvedite 0 : '))
max_sum = 0
while num != 0:
    sum = 0
    n = num
    while num % 10 != 0 or num // 10 != 0:
        sum += num % 10
        num //= 10
    if sum > max_sum:
        max_sum = sum
        max_num = n
    num = int(input('vvedote tseloe chislo. dlya vihoda vvedite 0 : '))
print(f'v chisle {max_num} maximalnaya suuma tsifr : {max_sum}')