# 7. По длинам трех отрезков, введенных пользователем, определить возможность существования треугольника,
# составленного из этих отрезков. Если такой треугольник существует, то определить,
# является ли он разносторонним, равнобедренным или равносторонним.

print('vvedite dlinu 3 otrezkov:')
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))

if a + b >= c and a + c >= b and b + c >= a:
    if a == b or b == c or c == a:
        if a == b and a == c:
            print('ravnostoronniy treugolnik')
        else:
            print('ravnobedrenny treugolnik')
    else:
        print('raznostoronniy treugolnik')
else:
    print('treugolnik ne poluchaetsya s takimi dlinami')