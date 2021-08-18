# 1. Написать программу, которая будет складывать, вычитать, умножать или делить два числа.
# Числа и знак операции вводятся пользователем.
# После выполнения вычисления программа не должна завершаться, а должна запрашивать новые данные для вычислений.
# Завершение программы должно выполняться при вводе символа '0' в качестве знака операции.
# Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'),
# то программа должна сообщать ему об ошибке и снова запрашивать знак операции.
# Также сообщать пользователю о невозможности деления на ноль, если он ввел 0 в качестве делителя.

operator1 = int(input("vvedite 1 operator : "))
operator2 = int(input("vvedite 2 operator : "))
operand = str(input("vvedite operatsiyu '+', '-', '*', '/' (dlya vihoda vvedite '0' : "))
while operand != "0":
    result = "n/a"
    if operand == "+":
        result = operator1 + operator2
    elif operand == "-":
        result = operator1 - operator2
    elif operand == "*":
        result = operator1 * operator2
    elif operand == "/":
        if operator2 != 0:
            result = operator1 / operator2
        else:
            print("na nol nelzya delit ")
    else:
        print("nepravilniy vvod operatsii poprobuyte eshe raz ")
    print(f"{operator1} {operand} {operator2} = {result}")
    operator1 = int(input("vvedite 1 operator : "))
    operator2 = int(input("vvedite 2 operator : "))
    operand = str(input("vvedite operatsiyu '+', '-', '*', '/' (dlya vihoda vvedite '0' : "))
print("vihod vipolnen uspeshno")