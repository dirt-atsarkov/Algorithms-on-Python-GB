# Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран. Например, если введено число 3486, то надо вывести число 6843.
number = int(input("vvedite tseloe chislo : "))

def reverse(n):
    if n < 10:
        return n
    else:
        rev = str(n % 10) + str(reverse(n // 10))
        return rev

print(reverse(number))