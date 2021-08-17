#Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

a = int(input('Введите трехзначное число '))

summ = 0
mult = 1

if a <= 999 and a >= 100 :
    summ += a % 10
    mult *= a % 10
    a = a // 10
    summ += a % 10
    mult *= a % 10
    summ += a // 10
    mult *= a // 10
    print('summa : ', summ)
    print('proizvedenie :', mult)

else :
    print('введено не 3-х значное число')