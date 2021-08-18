# Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
# Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.

length = int(input('vvedite dlinu posledovatelnosti :  '))
num = int(input('vvedite tsifru dlya proverki vhozhdeniy : '))
count = 0
for i in range(length):
    m = int(input(f'vvedite chislo : '))
    while m > 0:
        if m % 10 == num:
            count += 1
        m = m // 10
print(f'vhozhdeniy chisla {num} v posledovatelnost : {count} raz')

