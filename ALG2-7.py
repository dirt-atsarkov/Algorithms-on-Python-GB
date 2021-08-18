# Напишите программу, доказывающую или проверяющую, что для множества натуральных чисел выполняется равенство:
# 1+2+...+n = n(n+1)/2, где n - любое натуральное число.

number = int(input("vvedite chislo : "))

def factorial(n):
    b = 0
    for i in range(1, n+1):
        b += i
    return(b)

if int(factorial(number)) == int(number*(number + 1)/2):
    print("ok")
else:
    print("not ok")