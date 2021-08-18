# В программе генерируется случайное целое число от 0 до 100.
# Пользователь должен его отгадать не более чем за 10 попыток.
# После каждой неудачной попытки должно сообщаться больше или меньше введенное пользователем число, чем то, что загадано.
# Если за 10 попыток число не отгадано, то вывести загаданное число.

import random

number_user = int(input("ugadayte zagadannoe chislo ot 0 do 100 : "))
number = random.randint(0, 100)

i = 10

while i > 0:
    if number > number_user:
        number_user = int(input("bolshe : "))
    elif number < number_user:
        number_user = int(input("menshe : "))
    else: break
    i -= 1

print(f"chislo bilo : {number}")