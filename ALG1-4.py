#Написать программу, которая генерирует в указанных пользователем границах
#случайное целое число,
#случайное вещественное число,
#случайный символ.
#Для каждого из трех случаев пользователь задает свои границы диапазона.
# Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
# Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.


import random

print("vvedite granitsy dlya generatsii tselogo chisla :")
x1 = int(input("x1 = "))
x2 = int(input("x2 = "))

print("vvedite granitsy dlya generatsii veshestvennogo chisla :")
y1 = float(input("y1 = "))
y2 = float(input("y2 = "))

print("vvedite dve bukvy dlya zadania granits generatsii simvola :")
l1 = (input("l1 = ")).upper()
l2 = (input("l2 = ")).upper()


print(f'Tseloe chislo: {random.randint(x1, x2)}\n'
      f'Veshestvennoe chislo: {random.uniform(y1, y2)}\n'
      f'Simvol: {chr(random.randint(ord(l1), ord(l2)))}')