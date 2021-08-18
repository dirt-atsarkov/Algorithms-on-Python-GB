# Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

number = input("vvedite tseloe chislo : ")
chet = 0
nechet = 0

for digit in number:
    if int(digit) % 2 == 0:
        chet += 1
    else:
        nechet += 1

print(f"v chisle {number} : {chet} chetnikh tsifr i {nechet} nechetnikh tsifr")