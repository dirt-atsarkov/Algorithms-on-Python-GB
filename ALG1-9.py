# Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

print('vvedite 3 chisla : ')
a = int(input('a : '))
b = int(input('b : '))
c = int(input('c : '))

summ = a + b + c
mid = summ - max(a, b, c) - min(a, b, c)

print(f'srednee chislo : {mid}')